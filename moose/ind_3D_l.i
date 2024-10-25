E =  139 #139
K =  7.26 #7.26
n =  0.195 #0.195
hm = 0.226 #0.226
nu = 0.25

fname = mesh/3D_r0.e

# substrate refinement
ref = 0
# indenter refinement
refi = 0

[GlobalParams]
  displacements = 'disp_x disp_y disp_z'
  volumetric_locking_correction = true
  order = FIRST
  family = LAGRANGE
[]
  
[Mesh]
  [initial]
    type = FileMeshGenerator
    file = ${fname}
  []
  [refine]
    type = RefineBlockGenerator
    input = initial
    block = '1 2'
    refinement = '${ref} ${refi}'
  []
  [convert_to_linear]
    type = ElementOrderConversionGenerator
    input = refine
    conversion_type = FIRST_ORDER
  []
[]
  
[Functions]
  [push_down]
    type = PiecewiseLinear
    xy_data = '0    0
                1   -${hm}
                1.5  0'
  [] #Indenter displacement, μm
[]

[AuxVariables]
  [saved_x]
  []
  [saved_y]
  []
  [saved_z]
  []
  [effective_plastic_strain]
    order = FIRST
    family = MONOMIAL
  []
  [SED]
    order = CONSTANT
    family = MONOMIAL
  []
[]
  
[AuxKernels]
  [effective_plastic_strain]
    type = MaterialRealAux
    variable = effective_plastic_strain
    property = effective_plastic_strain
    block = 1
  []
  [strain_energy]
    type = MaterialRealAux
    variable = SED
    property = strain_energy_density
    execute_on = timestep_end
    block = 1
  []
[]
  
[Physics/SolidMechanics/QuasiStatic]
  [all]
    add_variables = true
    new_system = true
    formulation = TOTAL
    strain = FINITE
    block = '1 2'
    generate_output = 'stress_xx stress_xy stress_xz stress_yy stress_zz vonmises_stress'
    material_output_order = FIRST
    save_in = 'saved_x saved_y saved_z'
  []
[]
  
[BCs]
  [specimen_y]
    type = DirichletBC
    variable = disp_y
    boundary = 1
    value = 0.0
  []

  [indenter_0]
    type = DirichletBC
    variable = disp_z
    boundary = 2
    value = 0.0
  []
  [specimen_0]
    type = DirichletBC
    variable = disp_z
    boundary = 6
    value = 0.0
  []
  [InclinedNoDisplacementBC]
    [indenter_60]
    boundary = 3
    penalty = 5e3#1e4#1e3
    displacements = 'disp_x disp_y disp_z'
    []
    [specimen_60]
    boundary = 7
    penalty = 5e3#1e4#1e3
    displacements = 'disp_x disp_y disp_z'
    []
  []
  
  [indenter_y]
    type = FunctionDirichletBC
    variable = disp_y
    boundary = 8
    function = push_down
  []
[]
  
[Materials]
  [tensor]
    type = ComputeIsotropicElasticityTensor
    block = '2'
    youngs_modulus = 1143 #E, GPa
    poissons_ratio = 0.0691 #ν
  []
  [stress]
    type = ComputeFiniteStrainElasticStress
    block = '2'
  []
  [stress_wrapped]
    type = ComputeLagrangianWrappedStress
  []

  [tensor_2]
    type = ComputeIsotropicElasticityTensor
    block = '1'
    youngs_modulus = ${E} #139 #E, GPa
    poissons_ratio = ${nu} #0.25 #ν
  []
  [power_law_hardening]
    type = IsotropicPowerLawHardeningStressUpdate
    strength_coefficient = ${K} #7.26 #K, GPa
    strain_hardening_exponent = ${n} #0.195 #n
    block = '1'
  []
  [radial_return_stress]
    type = ComputeMultipleInelasticStress
    inelastic_models = 'power_law_hardening'
    block = '1'
  []
  [strain_energy_density]
    type = StrainEnergyDensity
    incremental = true
    block = 1
  []
[]
  
[Postprocessors]
  [W]
    type = ElementIntegralMaterialProperty
    mat_prop = strain_energy_density
    block = 1
  []
  [stress_yy]
    type = ElementAverageValue
    variable = stress_yy
    block = 1
  []
  [react_y_top]
    type = NodalSum
    variable = saved_y
    boundary = 8
  []
  [disp_y_top]
    type = NodalExtremeValue
    variable = disp_y
    boundary = 8
  []
  [h]
    type = AverageElementSize
    outputs = 'console'
    execute_on = 'timestep_end'
    block = '1 2'
  []
[]

# [VectorPostprocessors]
#   [y_disp]
#     type = NodalValueSampler
#     variable = disp_y
#     block = '1'
#     sort_by = x
#   []
# []
  
[Executioner]
  type = Transient
  solve_type = 'PJFNK'

  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre    boomeramg'
#  petsc_options_iname = '-pc_type -pc_factor_mat_solver_type'
#  petsc_options_value = 'lu    superlu_dist'
  line_search = 'none'
  petsc_options = '-snes_ksp_ew'

  l_max_its = 20
  nl_max_its = 50
  dt = 0.01
  dtmin = 0.00001
  end_time = 1.5
  nl_rel_tol = 1e-6
  nl_abs_tol = 1e-10
  automatic_scaling = true
  [Predictor]
    type = SimplePredictor
    scale = 1.0
    skip_times_old = 1.0
  []
[]

[Outputs]
  [out] # This makes a smaller exodus file with only three points of interest
    type = Exodus
    sync_times = '1.0 1.01 1.5'
    sync_only = true
  []
  # exodus = true
  # [checkpoint] # This keeps the checkpoint from forming 
  #   type = Checkpoint
  #   sync_times = ''
  #   sync_only = true
  #   num_files = 1
  # []
  # [csv] # This makes a smaller exodus file with only three points of interest
  #   type = CSV
  #   sync_times = '1.0 1.01 1.5'
  #   sync_only = true
  # []
  csv = true
  print_linear_residuals = true
  print_perf_log = true
  [console]
    type = Console
    max_rows = 5
  []
  # set file_base to choose what it's named
  file_base = '3D_l_${refi}_${ref}'
[]

[Preconditioning]
  [smp]
    type = SMP
    full = true
  []
[]
  
[Dampers]
  [contact_slip]
    type = ContactSlipDamper
    primary = '5'
    secondary = '4'
    min_damping_factor = 0.01
  []
  [jacobian]
    type = ElementJacobianDamper
    max_increment = 0.01
  []
[]
  
[Contact]
  [ind_base]
    primary = 5
    secondary = 4
    model = coulomb
    friction_coefficient = 0.4
    normalize_penalty = true
    formulation = penalty #tangential_penalty
    # Set penalty here and in InclinedNoDisplacementBC lower if solution does not converge
    penalty = 5e3#1e4
    normal_smoothing_distance = 0.1
    tangential_tolerance = 1e-1
  []
[]

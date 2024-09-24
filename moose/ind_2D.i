E =  139 #139
K =  7.26 #7.26
n =  0.195 #0.195
# Pm = 10 #10
hm = 0.226 #0.226
nu = 0.25
# For coarse meshes, you may need to decrease contact penalty to 1e3 
fname = 2D_refq.e

[GlobalParams]
  displacements = 'disp_x disp_y'
  volumetric_locking_correction = true
  order = SECOND
  family = LAGRANGE
[]
  
[Mesh]
  coord_type = RZ
  [initial]
    type = FileMeshGenerator
    file = ${fname}
  []
[]
  
[Functions]
  [push_down]
    type = PiecewiseLinear
    xy_data = '0    0
                1   -${hm}
                1.5  0'
  [] #Indenter displacement, μm. 0.226 is average.
  # [push_down]
  #   type = PiecewiseLinear
  #   xy_data = '0  0
  #             1 -${fparse Pm/6}
  #             1.5 0'
  # [] # Indenter maximum load, mN. 10
[]

[AuxVariables]
  [saved_x]
  []
  [saved_y]
  []
  [effective_plastic_strain]
    order = SECOND
    family = MONOMIAL
  []
[]
  
[AuxKernels]
  [effective_plastic_strain]
    type = ADMaterialRealAux
    variable = effective_plastic_strain
    property = effective_plastic_strain
    block = 2
  []
[]
  
[Physics/SolidMechanics/QuasiStatic]
  [all]
    add_variables = true
    strain = FINITE # For large deformations
    block = '1 2'
    use_automatic_differentiation = true
    generate_output = 'stress_xx stress_xy stress_xz stress_yy stress_zz vonmises_stress'
    save_in = 'saved_x saved_y'
    use_finite_deform_jacobian = true
  []
[]
  
[BCs]
  [specimen_y]
    type = DirichletBC
    variable = disp_y
    boundary = 6
    value = 0.0
  []

  [symm_x_indenter]
    type = DirichletBC
    variable = disp_x
    boundary = 4
    value = 0.0
  []
  [symm_x_material]
    type = DirichletBC
    variable = disp_x
    boundary = 7
    value = 0.0
  []    

  [indenter_y]
    type = FunctionDirichletBC
    # type = FunctionNeumannBC
    variable = disp_y
    boundary = 1
    function = push_down
  []
[]
  
[Materials]
  [tensor]
    type = ADComputeIsotropicElasticityTensor
    block = '1'
    youngs_modulus = 1143 #E, GPa
    poissons_ratio = 0.0691 #ν
  []
  [stress]
    type = ADComputeFiniteStrainElasticStress
    block = '1'
  []

  [tensor_2]
    type = ADComputeIsotropicElasticityTensor
    block = '2'
    youngs_modulus = ${E} #139 #E, GPa
    poissons_ratio = ${nu} #0.25 #ν
  []
  [power_law_hardening]
    type = ADIsotropicPowerLawHardeningStressUpdate
    strength_coefficient = ${K} #7.26 #K, GPa
    strain_hardening_exponent = ${n} #0.195 #n
    block = '2'
  []
  [radial_return_stress]
    type = ADComputeMultipleInelasticStress
    inelastic_models = 'power_law_hardening'
    block = '2'
  []
[]
  
[Postprocessors]
  [stress_yy]
    type = ElementAverageValue
    variable = stress_yy
    block = 2
  []
  [react_y_top]
    type = NodalSum
    variable = saved_y
    boundary = 1
  []
  [disp_y_top]
    type = NodalExtremeValue
    variable = disp_y
    boundary = 1
  []
  [h]
    type = AverageElementSize
    outputs = 'console'
    execute_on = 'timestep_end'
    block = '1 2' 
  []
[]
  
[Executioner]
  type = Transient
  solve_type = 'PJFNK'

  petsc_options_iname = '-pc_type -pc_factor_mat_solver_type'
  petsc_options_value = 'lu    superlu_dist'
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
  exodus = true
  csv = true
  print_linear_residuals = true
  print_perf_log = true
  [console]
    type = Console
    max_rows = 5
  []
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
    primary = '2'
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
    primary = 2
    secondary = 4
    model = coulomb
    friction_coefficient = 0.4
    normalize_penalty = true
    formulation = penalty
    # Set penalty lower if solution does not converge
    penalty = 1e4#1e3
    #capture_tolerance = 1e-4
    tangential_tolerance = 1e-1
  []
[]  
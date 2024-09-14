
[Mesh]
  # Boundaries: left = 1, top = 2, right = 3, bottom = 4, corner = 5
  [mesh]
    type = FileMeshGenerator
    file = 'toy_mesh_l0.e'
  []
[]

[GlobalParams]
  order = FIRST
  family = LAGRANGE
[]

[Variables]
  [disp_x]
  []
  [disp_y]
  []
[]

[AuxVariables]
  [stress_yy]
    order = CONSTANT
    family = MONOMIAL
  []
[]

[AuxKernels]
  [stress_yy]
    type = RankTwoAux
    variable = stress_yy
    rank_two_tensor = stress
    index_i = 1
    index_j = 1
    execute_on = timestep_end
  []
[]

[Postprocessors]
  [top_displacement]
    type = SideAverageValue
    variable = disp_y
    boundary = 2
  []
  [total_reaction_force]
    type = SideIntegralVariablePostprocessor
    variable = stress_yy
    boundary = 4
  []
[]

[VectorPostprocessors]
  [y_disp]
    type = NodalValueSampler
    variable = disp_y
    sort_by = x
  []
[]

[Kernels]
  [TensorMechanics]
    displacements = 'disp_x disp_y'
  []
[]

[BCs]
  [bottom_y]
    type = DirichletBC
    variable = disp_y
    boundary = 4
    value = 0
  []
  [bottom_x]
    type = DirichletBC
    variable = disp_x
    # Use boundary 5 for pin, boundary 4 for fixed
    boundary = 4
    value = 0
  []
#   [top_y]
#     type = FunctionNeumannBC
#     variable = disp_y
#     boundary = 2
#     function = '-1e8*t'
#   []
  [top_y]
    type = FunctionDirichletBC
    variable = disp_y
    boundary = 2
    function = '-0.1*t*sin(pi*x)'
  []
[]

[Materials]
  [elasticity]
    type = ComputeIsotropicElasticityTensor
    youngs_modulus = 1e9
    poissons_ratio = 0.3
  []
  [strain]
    type = ComputeSmallStrain
    displacements = 'disp_x disp_y'
  []
  [stress]
    type = ComputeLinearElasticStress
  []
[]

[Executioner]
  type = Transient
  dt = 0.1
  end_time = 1.0
  solve_type = PJFNK
  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre boomeramg'
[]

[Outputs]
  exodus = true
  csv = true
[]
name = '1'
E = 200e9
nu = 0#.3
b = 100#e9
tb = 100#e9
A = 1
ref = 0

[Mesh]
  [mesh]
    type = FileMeshGenerator
    # file = mesh/toy_mesh_l0tri.e
    file = mesh/toy_mesh_l0.e
    # file = mesh/toy_mesh_q0.e
  []
  [refine]
    type = RefineBlockGenerator
    input = mesh
    block = 1
    refinement = ${ref}
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
  [error]
    type = ElementL2Error
    variable = disp_y
    function = exact
  []
[]

[Functions]
  [body_force]
    type = ParsedFunction
    # Constant body load
    # value = '${b}*t'
    # Varied body load
    value = '${b}*y*t'
  []
  [exact] # For use in calculating the exact solution for the toy problem
    type = ParsedFunction
    # Compression test
    # expression = '(1-${nu}^2)/(${A}*${E})*-y*${tb}'
    # Constant body load
    # expression = '(1/(${E}*${A}))*((-((y)^2)*${b}/2))'
    # Linearly varying load
    expression = '(1/(${E}*${A}))*((-((y)^3)*${b}/6)-(y*${tb}/2))'
  []
[]

[Kernels]
  [TensorMechanics]
    displacements = 'disp_x disp_y'
    use_displaced_mesh = true
  []
  [BodyForce]
    type = ADBodyForce
    variable = disp_y
    block = 1
    function = body_force
    use_displaced_mesh = true
  []
[]

[BCs]
  # Boundaries: left = 1, top = 2, right = 3, bottom = 4, corner = 5
  [bottom_y]
    type = DirichletBC
    variable = disp_y
    boundary = 4
    value = 0
  []
  [bottom_x]
    type = DirichletBC
    variable = disp_x
    # Use boundary 5 for pin, boundary 4 for glued, boundary 1, 3, 4 for fixed at three ends.
    boundary = 5
    value = 0
  []
  [top_y] # Constant axial load case
    type = FunctionNeumannBC
    variable = disp_y
    boundary = 2
    function = '-${tb}*t'
  []
[]

[Materials]
  [elasticity] # Near properties of structural steel
    type = ComputeIsotropicElasticityTensor
    youngs_modulus = ${E}
    poissons_ratio = ${nu}
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
  dt = 1.0
  end_time = 1.0
  solve_type = PJFNK
  # petsc_options_iname = '-pc_type -pc_factor_mat_solver_package'
  # petsc_options_value = 'lu mumps'
  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre boomeramg'
  # solve_type = NEWTON
  # petsc_options_iname = '-pc_type -ksp_type'
  # petsc_options_value = 'asm gmres'
[]

[Outputs]
  exodus = true
  # csv = true
  file_base = 'toyproblem_${name}_${ref}'
[]
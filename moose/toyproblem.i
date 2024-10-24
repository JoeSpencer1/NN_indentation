E = 200e9
nu = 0.3
c = 1e9
l = 0.5
A = 1
ref = 0

[Mesh]
  # Boundaries: left = 1, top = 2, right = 3, bottom = 4, corner = 5
  [mesh]
    type = FileMeshGenerator
    file = outputs/toyproblem/toy_mesh_l0.e
  []
  [refine]
    type = RefineBlockGenerator
    input = mesh
    block = 1#'1 2'
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

[VectorPostprocessors]
  [y_disp]
    type = NodalValueSampler
    variable = disp_y
    sort_by = y
  []
[]

[Functions]
  # [body_force]
  #   type = ParsedFunction
  #   value = '${c}*y*t'
  # []
  [exact] # For use in calculating the exact solution for the toy problem
    # c=1e8, l=0.5, A=1, E=200e9
    type = ParsedFunction
    expression = '(${c}/(${E}*${A}))*(-(y^3)/6+y*${l}^2)'
  []
[]

[Kernels]
  [TensorMechanics]
    displacements = 'disp_x disp_y'
    use_displaced_mesh = true
  []
  # [BodyForce]
  #   type = ADBodyForce
  #   variable = disp_y
  #   block = 1
  #   function = body_force
  #   use_displaced_mesh = true
  # []
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
    # Use boundary 5 for pin, boundary 4 for glued
    boundary = 5
    value = 0
  []
  [top_y] # Constant axial load case
    type = FunctionNeumannBC
    variable = disp_y
    boundary = 2
    function = '-1e8*t'
  []
  # [top_y] # Linearly varied axial load case
  #   type = FunctionNeumannBC
  #   variable = disp_y
  #   boundary = 2
  #   function = '-2e8*t*x'
  # []
  # [top_y] # Fish book problem. c=1e8, l=0.5, A=1
  #   type = FunctionNeumannBC
  #   variable = disp_y
  #   boundary = 2
  #   function = '-${c}*((${l}^2)/${A})*t'
  # []
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
  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre boomeramg'
[]

[Outputs]
  exodus = true
  csv = true
[]
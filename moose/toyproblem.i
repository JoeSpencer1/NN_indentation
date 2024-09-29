E = 200e9
nu = 0#0.3
c = 1e8
l = 0.5
A = 1

[Mesh]
  # Boundaries: left = 1, top = 2, right = 3, bottom = 4, corner = 5
  [mesh]
    type = FileMeshGenerator
    file = 'toy_mesh_q7.e'
  []
  # [refine]
  #   type = RefineBlockGenerator
  #   input = mesh
  #   block = 1 
  #   refinement_type = uniform
  #   refinement = 1  
  # # []
[]

[GlobalParams]
  order = SECOND
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

# [VectorPostprocessors]
#   [y_disp]
#     type = NodalValueSampler
#     variable = disp_y
#     sort_by = x
#   []
# []

[Functions]
  [body_force]
    type = ParsedFunction
    value = '${c}*y*t'
  []
[]

[Kernels]
  [TensorMechanics]
    displacements = 'disp_x disp_y'
  []
  [BodyForce]
    type = ADBodyForce
    variable = disp_y
    block = 1
    function = body_force
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
    # Use boundary 5 for pin, boundary 4 for glued
    boundary = 5
    value = 0
  []
  # [top_y] # Constant axial load case
  #   type = FunctionNeumannBC
  #   variable = disp_y
  #   boundary = 2
  #   function = '-1e8*t'
  # []
  # [top_y] # Varied axial load case
  #   type = FunctionNeumannBC
  #   variable = disp_y
  #   boundary = 2
  #   function = '-2e8*t*x'
  # []
  [right_y] # Fish book problem. c=1e8, l=0.5, A=1
    type = FunctionNeumannBC
    variable = disp_y
    boundary = 2
    function = '-${c}*((${l}^2)/${A})*t'
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
  petsc_options_iname = '-pc_type -pc_hypre_type'
  petsc_options_value = 'hypre boomeramg'
[]

[Outputs]
  exodus = true
  csv = true
[]
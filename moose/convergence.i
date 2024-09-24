# 3D case
# h_1 = 0.1769296 # linear
# h_1 = 0.1923527 # quad
# h_2 = 0.3896965
# # 2D case
# h_1 = 9.082717e-02
# h_2 = 0.1769296
h_1 = 0.25
h_2 = 0.5
# h_1 = 4.622396e-02
# h_2 = 0.09082717#0.1769296

current_refine = outputs/convergence/3D_rl2.e
most_refined = outputs/convergence/3D_refl.e
second_refined = outputs/convergence/3D_rl2.e#3D_rq2.e


[Mesh]
  # This is the input or ou
  tput mesh for whichever refinement level you want to integrate
  file = ${current_refine} #${most_refined}
  block = '1 2'
[]

[GlobalParams]
  order = FIRST
  family = LAGRANGE
[]

[Problem]
  solve = false
[]

[AuxVariables]
  [dummy]
    initial_condition = 0
  []
  [disp_y_1]
  []
  [disp_y_2]
  []
  [disp_y_n]
  []
[]

[AuxKernels]
  [disp_y_1]
    type = FunctionAux
    variable = disp_y_1
    function = function_1
  []
  [disp_y_2]
    type = FunctionAux
    variable = disp_y_2
    function = function_2
  []
  [disp_y_n]
    type = FunctionAux
    variable = disp_y_n
    function = function_n
  []
[]

[Materials]
  [toperror]
    type = ParsedMaterial
    property_name = 'toperror'
    coupled_variables = 'disp_y_1 disp_y_2 disp_y_n'
    expression = '(((${h_2}/${h_1})^2*disp_y_1 - disp_y_2) / ((${h_2}/${h_1})^2 - 1) - disp_y_n)^2'
    outputs=all
  []
  [bottomerror]
    type = ParsedMaterial
    property_name = 'bottomerror'
    coupled_variables = 'disp_y_1 disp_y_2'
    expression = '(((${h_2}/${h_1})^2*disp_y_1 - disp_y_2) / ((${h_2}/${h_1})^2 - 1))^2'
  []
[]

[Functions]
  [function_1]
    type = SolutionFunction
    solution = solution_1
    from_variable = 'disp_y'
  []
  [function_2]
    type = SolutionFunction
    solution = solution_2
    from_variable = 'disp_y'
  []
  [function_n]
    type = SolutionFunction
    solution = solution_n
    from_variable = 'disp_y'
  []
[]

[UserObjects]
  [solution_1]
    type = SolutionUserObject
    system_variables = 'disp_x disp_y'
    # system_variables = 'disp_x disp_y disp_z'
    # This is the output mesh with the most refined solution
    mesh = ${most_refined}
  []
  [solution_2]
    type = SolutionUserObject
    system_variables = 'disp_x disp_y'
    # system_variables = 'disp_x disp_y disp_z'
    # This is the output mesh with the second most refined solution
    mesh = ${second_refined}
  []
  [solution_n]
    type = SolutionUserObject
    system_variables = 'disp_x disp_y'
    # system_variables = 'disp_x disp_y disp_z'
    # This is the output mesh with the nth refined solution that you compute the error on
    mesh = ${current_refine}
  []
[]

[Postprocessors]
#   [richardson_error]
#     type = RichardsonExtraplationError
#     variable = dummy
#     function_1 = function_1
#     function_2 = function_2
#     function_n = function_n
#   []
#   [rel_error]
#     type = ElementL2Error
#     variable = disp_y_n
#     function = function_1
#   []
  [richardson_top]
    type = ElementIntegralMaterialProperty
    mat_prop = toperror
    block = '1 2'
  []
  [richardson_bottom]
    type = ElementIntegralMaterialProperty
    mat_prop = bottomerror
    block = '1 2'
  []
[]

# [VectorPostprocessors]
#   [convergence_disp]
#     type = PointValueSampler
#     use_interpolated_state = true
#     variable = disp_y_n
#     points = '0.5	0.5	0
#             0.5	0.625	0
#             0.625	0.625	0
#             0.625	0.5	0'
#     sort_by = x
#   []
# []

[Executioner]
  type = Transient
  #Use time stepping to match your solutions. They don't have to match -- it will interpolate if
  #they don't match.
  start_time = 0.0
  end_time = 1.0
  dt = 0.01
[]

[Outputs]
#   file_base = out
  exodus = true
  csv = true
  [convfile]
    type = CSV
    show = 'disp_y_n'
    execute_on = final
    execute_vector_postprocessors_on = FINAL
  []
[]
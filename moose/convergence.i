h_1 = 0.0078125
h_2 = 0.015625

E = 200e9
c = 1e9
l = 0.5
A = 1

current_refine = toyproblemq2.e

most_refined = toyproblemq7.e
second_refined = toyproblemq6.e
ref_refine = toyproblemq7.e


[Mesh]
  # This is the input or output mesh for whichever refinement level you want to integrate
  file = ${ref_refine}
  block = 1#'1 2'
[]

[GlobalParams]
  order = SECOND
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

  [exact] # For use in calculating the exact solution for the toy problem
    # c=1e8, l=0.5, A=1, E=200e9
    type = ParsedFunction
    expression = '(${c}/(${E}*${A}))*(-(y^3)/6+y*${l}^2)'
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
  [rich_top]
    type = ElementIntegralMaterialProperty
    mat_prop = toperror
    block = 1#'1 2'
  []
  [rich_bottom]
    type = ElementIntegralMaterialProperty
    mat_prop = bottomerror
    block = 1#'1 2'
  []
  [rich_normal]
    type = ParsedPostprocessor
    function = 'sqrt(rich_top/rich_bottom)'
    pp_names = 'rich_top rich_bottom'
  []
  [rich_error]
    type = ParsedPostprocessor
    function = 'sqrt(rich_top)'
    pp_names = 'rich_top rich_bottom'
  []

  [error]
    type = ElementL2Error
    variable = disp_y_n
    function = exact
  []
[]

[VectorPostprocessors]
#   [convergence_disp] # ElementMaterialsSampler is not in local moose copy.
#     type = ElementMaterialSampler
#     material = 'toperror'
#     block = '1'
#   []
  # [convergence_disp]
  #   type = PointValueSampler
  #   use_interpolated_state = true
  #   variable = disp_y_n
  #   points = '0.25	0.25	0'
  #   sort_by = x
  # []
[]

[Executioner]
  type = Transient
  #Use time stepping to match your solutions. They don't have to match -- it will interpolate if
  #they don't match.
  start_time = 0.0
  end_time = 1.0
  dt = 1.0
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
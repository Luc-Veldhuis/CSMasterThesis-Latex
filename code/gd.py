output = condition.get_output()
repick_counter = 0
gradient = Gradient(condition.offsets)
for i in max_iterations:
    output = gradient_iteration(output)
    
def gradient_iteration():
    calculate_gradient()
    while gradient.max() == 0 and repick_counter < max_repicks:
        output = repick_startpoint()
        calculate_gradient()
    gradient.normalize()
    return descend()
    
def calculate_gradient():
    for i in len(gradient)
        partial_derivative(gradient[i])
    
def partial_derivative(gradient_direction):
    new_value_plus_one = get_output(gradient_direction, output, 1)
    new_value_minus_one = get_output(gradient_direction, output, -1)
    arg1_original = run(output)
    arg1_plus_one = run(new_value_plus_one)
    arg1_minus_one = run(new_value_minus_one)
    gradient[i].delta = arg1_original - min(arg1_original, arg1_plus_one, arg1_minus_one)
    
def descend():
    for i in len(gradient):
        output = get_output(gradient_direction, output, gradient[i].delta*percentage)
    return run(output)
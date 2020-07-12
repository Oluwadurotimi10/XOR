# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:19:02 2020

@author: JADESOLA
"""

import pandas as pd

# TODO: Set weight1, weight2, and bias
weight_nand1 = -20.0
weight_nand2 = -20.0
bias_nand = 30.0
weight_or1 = 20.0
weight_or2 = 20.0
bias_or = -10.0
weight_and1 = 20.0
weight_and2 = 20.0
bias_and = -30.0


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, True, True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    #the model for the or perceptron
    linear_combination1 = weight_or1 * test_input[0] + weight_or2 * test_input[1] + bias_or
    
    #the model for the nand perceptron
    linear_combination2 = weight_nand1 * test_input[0] + weight_nand2 * test_input[1] + bias_nand
    
    #the hidden layer 
    perceptron1 = int(linear_combination1 >= 0)
    perceptron2 = int(linear_combination2 >= 0)
    
    #the model for the and perceptron
    linear_combination_final =  weight_and1 * perceptron1 + weight_and2 * perceptron2 + bias_and
    output = int(linear_combination_final >= 0)
    
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination_final, output, is_correct_string])
        
# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))

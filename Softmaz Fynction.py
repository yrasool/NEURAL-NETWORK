#softmax activation
import math
import numpy as np
layer_outputs = [4.8, 1.21, 2.385] #this is the output of the first layer

layer_outputs = [4.8, 4.79, 4.25] #this is the output of the first layer

#the above two outputs are the output of the first layer and
# we will figure out how wrong they are

#we will use the softmax activation function to figure out how wrong the output is
#exponential function is used to make the values positive even if we get negatuve values
E = math.e

exp_values = np

#or instead of using numy exp function we use math module
for output in layer_outputs:
    exp_values.append(E**output)
    
print(f'exponentiated values:'{exp_values})

#After exponentiating the values we need to normalize them between 0 and 1
#a single output neuron is divided by the sum of all the output neurons
#also we subtract the largest value from the exponentiated values to avoid overflow
norm_value = exp_values/np.sum(exp_values)

#or 
#norm_base = sum(exp_values)
#norm_values = []

#for value in exp_values:
    #norm_values.append(value/norm_base)
    
#print(norm_values)
#print(sum(norm_values))
 


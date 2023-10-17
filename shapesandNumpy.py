# Dot product allows us to multiply two vectors together multiplying each element of one vector by the corresponding element of the other vector and then summing the results.
#the dot product provides us a scalar value that we can use to compare two vectors.
import numpy as np


input = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
bias = 3.0

output = np.dot(weights, input) + bias
print(output)

# because we want result to be indexed by the neuron number, we need to transpose the weights matrix
# we have three neurons, so we want a 3x1 matrix

# np.dot(weights, input) = (np.dot(weights[0], input), np.dot(weights[1], input), np.dot(weights[2], input))
# we wiil get an array of 3 elements
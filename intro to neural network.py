inputs = [1.5,3, 5.1, 2.2]

weight1 = [0.3, 0.2, -0.9, 0.5]
weight2 = [0.4, 0.3, 0.5, 0.1]
weight3 = [0.7, -0.6, 0.4, 0.9]

bias1 = 3 # bias is a constant value which is added to the weighted sum of inputs and weights so that the neuron can 
bias2 = 2 #learn when there is no input
bias3 = 0.5# there are three  biases because


weights = [[0.3, 0.2, -0.9, 0.5], [0.4, 0.3, 0.5, 0.1], [0.7, -0.6, 0.4, 0.9]] # we can use a list of lists to represent the weights

bias = [3, 2, 0.5] # we can use a list to represent the biases

#bias allows the neuron to fire even when all the inputs are zero meaning that the neuron can learn when there is no input\
output = [ inputs[0]*weight1[0] + inputs[1]*weight1[1] + inputs[2]*weight1[2] + bias[0],
            inputs[0]*weight2[0] + inputs[1]*weight2[1] + inputs[2]*weight2[2] + bias[1],
            inputs[0]*weight3[0] + inputs[1]*weight3[1] + inputs[2]*weight3[2] + bias[3]
]#1.5*3.2 + 5.1*2.2 + 2.2*8.8 + 3 = 50.39

layer_outputs = [] # output of current layer
for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0 # output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)







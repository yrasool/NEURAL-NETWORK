some_value = 0.5
weight = 0.7
bias = 0.7

print(some_value * weight )
print(some_value * weight + bias)

# the value of the bias is the threshold for the neuron to fire
# if the value is less than the bias, the neuron will not fire
#the change in value from the first print to the second print shows us if there is a
#negative or positive value bias will offset the value of the neuron
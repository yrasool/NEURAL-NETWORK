#because batches and layers are the most important parts of a neural network
#batches allow for the network to be trained on a small amount of data at a time

#layers are the different parts of the network that allow for the network to be trained on different parts of the data


# we have a single sample that has four features and a single label
# the features are the length,width, height, and weight of a single flower

inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
              [0.5, -0.91, 0.26, -0.5],
              [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)

# through batches we ask the neural network to make a prediction on a few samples at a time of the flower
 


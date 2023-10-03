#calculating loss with categorical crossentropy
#our output is  probability distribution and we want to compare 
# it with the target probability distribution
#the output is the probability of the input being in a particular class
#the purpose of the loss function is to compare the output probability distribution
#we do not get a binary output but a probability distribution

#closer to right value mean absolute error decresaes
#categorical cross entrop is the negative sum  of target probability distribution 
#multiplied by the log of the output probability distribution
#the formula is -sum(target * log(output)) ,
# where * is the dot product and the target is the one hot encoded vector
#an example of hot encoding is [0, 0, 1] for class 3 and [1, 0, 0] for class 1
import numpy as np
import math
b = 5.2
 
print(np.log(b))
print(math.e**1.6486586255873816)

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0])*target_output[0] + math.log(softmax_output[1])*target_output[1] + math.log(softmax_output[2])*target_output[2])
print(loss)
loss = -math.log(softmax_output[0])
print(loss)

print(-math.log(0.7))
print(-math.log(0.5))


import numpy as np

softmax_outputs = np.array([[0.7, 0.1, 0.2],
                            [0.1, 0.5, 0.4],     
                            [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1]

#Confidence on correct labels = [0,1,1] since the correct data is dog,cat and cat
#now we get from the output the confidence of the correct labels i.e [0.7,0.5,0.9]

print(softmax_outputs[[0, 1, 2], class_targets])

neg_log = -np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])


average_loss = np.mean(neg_log) 

#we have a problem, the - log of 0 is infinity and we cannot divide infinity by the number of samples
#we clip the values to a minimum value of 1e-7 because the log of 1e-7 is -16 which is a very small number
                  
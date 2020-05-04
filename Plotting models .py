#Instruction 1/4

import matplotlib.pyplot as plt
from keras.utils import plot_model

plot_model(model, to_file='model.png')

data = plt.imread('model.png')
plt.imshow(data)
plt.show()

#Instruction 2/4

#How many inputs does this model have? : 3

#Instruction 3/4

#How many outputs does this model have? : 1

#Instruction 4/4

#Which layer is shared between 2 inputs? : Team-Strength

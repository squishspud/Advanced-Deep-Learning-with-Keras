# Load the input layer from keras.layers
from keras.layers import Input

# Input layer for team 1
team_in_1 = Input(shape=(1,), name = 'Team-1-In')

# Separate input layer for team 2
team_in_2 = Input(shape=(1,), name = 'Team-2-In')

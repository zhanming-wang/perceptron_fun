import random
import numpy as np

INPUT = np.array([[1, 1], [0, 0], [1, 0], [0, 1]])
OUTPUT = np.array([1, 0, 0, 0])  # AND Gate
INPUT_NUM = INPUT.size
OUTPUT_NUM = OUTPUT.size
WEIGHT = np.array([random.random() for i in range(INPUT_NUM)])  # Randomly initialize weight
LEARNING_RATE = 0.1
EPOCH = 5

#   Activation
def step_function(weighted_sum):
    if weighted_sum > 0:
        return 1
    else:
        return 0


#   Forward Propagation
def forward(input_data, weight):
    y = np.array(step_function(np.dot(input_data, weight)))
    return y


#   Update Weight
#def weight_train(weight, epoch, learning_rate):
#    for ep in range(epoch):


import numpy as np
import math

def ReLU(input):
    return np.maximum(0, input)

def Sigmoid(input):
    try:
        return 1/(1+math.exp(-input))
    except OverflowError:
        print(input)
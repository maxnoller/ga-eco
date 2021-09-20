import numpy as np
import math
from numba import jit

@jit(nopython=True)
def ReLU(input):
    return np.maximum(0, input)

def Sigmoid(input):
    try:
        return 1/(1+np.exp(-input))
    except OverflowError:
        print(input)

def Linear(input):
    return input
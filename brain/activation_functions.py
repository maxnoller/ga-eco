import numpy as np
import math
from numba import jit

@jit(nopython=True)
def ReLU(input):
    return np.maximum(0, input)

@jit(nopython=True)
def Sigmoid(input):
    return 1/(1+math.exp(-input))
from .layers import Dense
from .activation_functions import Sigmoid, ReLU

class NeuralNetwork:
    def __init__(self, nrof_inputs, layers):
        self.layers = []
        prev_size = nrof_inputs
        for i in layers:
            self.layers.append(Dense(prev_size, i, Sigmoid))
            prev_size = i
    
    def forward_pass(self, inputs):
        current_value = inputs
        for layer in self.layers:
            current_value = layer.forward(current_value)
        return current_value

    def save(self, path):
        #TODO
        pass
    
    def load(self, path):
        #TODO
        pass
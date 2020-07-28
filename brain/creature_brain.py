import numpy as np

from .neural_network import NeuralNetwork

class Brain:
    def __init__(self, creature):
        self.network = NeuralNetwork(5, [10, 3])
        self.creature = creature

    def process_input(self, red, green, blue, hunger, health):
        return self.network.forward_pass(np.array([red,
                                                   green, 
                                                   blue, 
                                                   hunger, 
                                                   health]))
import numpy as np

from .neural_network import NeuralNetwork

class Brain:
    def __init__(self, creature):
        self.network = NeuralNetwork(14, [10, 3])
        self.creature = creature

    def process_input(self, tiles, hunger, health):
        return self.network.forward_pass(np.array([tiles[0][0],
                                                   tiles[0][1],
                                                   tiles[0][2],
                                                   tiles[1][0],
                                                   tiles[1][1],
                                                   tiles[1][2],
                                                   tiles[2][0],
                                                   tiles[2][1],
                                                   tiles[2][2],
                                                   tiles[3][0],
                                                   tiles[3][1],
                                                   tiles[3][2],
                                                   hunger, 
                                                   health]))
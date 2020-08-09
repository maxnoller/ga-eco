import numpy as np
import random

from .neural_network import NeuralNetwork

class Brain:
    def __init__(self, new_network=True):
        self.network = NeuralNetwork()
        self.network.create_layers(15, [20, 4])
    
    @staticmethod
    def from_existing_brain(brain):
        new_brain = Brain(new_network=False)
        new_brain.network = NeuralNetwork.from_network(brain.network)
        return new_brain

    def mutate(self):
        for layer in self.network.layers:
            for weight in layer.weights:
                if random.random() < 0.03:
                    weight += random.uniform(-1, 1) * weight
            for bias in layer.biases:
                if random.random() < 0.03:
                    bias += random.uniform(-1, 1) * bias

    def process_input(self, tiles, close_creatures, hunger, health):
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
                                                   close_creatures,
                                                   hunger, 
                                                   health]))
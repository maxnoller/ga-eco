import numpy as np

class Dense:
    def __init__(self, nrof_inputs, nrof_neurons, activation_function):
        self.weights = 0.1 * np.random.randn(nrof_inputs, nrof_neurons)
        self.biases = np.random.randn(1, nrof_neurons)
        self.activation_function = activation_function

    def forward(self, inputs):
        activation_values = np.dot(inputs, self.weights) + self.biases
        return np.array([self.activation_function(value) for value in activation_values[0]])

class Final:
    def __init__(self, nrof_inputs, nrof_neurons, activation_function):
        self.weights = 0.1 * np.random.randn(nrof_inputs, nrof_neurons)
        self.biases = np.random.randn(1, nrof_neurons)
        self.activation_function = activation_function

    def forward(self, inputs):
        activation_values = np.dot(inputs, self.weights) + self.biases
        return np.array([self.activation_function(value) for value in activation_values[0]])
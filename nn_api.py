import random
import numpy as np


class NeuralNet:
    weights = {}
    bias = {}

    def __init__(self, layers):
        self.layers = layers
        self.init_random_weights()

    @staticmethod
    def sigma(x):
        return 1 / (1 + np.exp(-x))

    def sigma_der(self, x):
        return self.sigma(x) * (1 - self.sigma(x))

    def init_random_weights(self):
        for i in range(len(self.layers) - 1):
            # each weights is the size of [l_1][l_0]
            random_weights = np.random.rand(self.layers[i + 1], self.layers[i])
            random_weights = (random_weights - 0.5) * 2
            self.weights[i] = random_weights
            # each bias is the size of [l_1][1]
            random_bias = np.random.rand(self.layers[i + 1], 1)
            random_bias = (random_bias - 0.5) * 2
            self.bias[i] = random_bias

    def vectorized_ff(self, x_vector):
        z = {}
        h = {}
        vector = x_vector
        for layer in range(len(self.layers) - 1):
            if layer > 0:
                ##
            z[layer] = np.dot(self.weights[layer], vector) + self.bias[layer]
            h[layer + 1] = self.sigma(z[layer])
        return h, z


# init net
nn_layers = [500, 100, 9]
nn = NeuralNet(nn_layers)

# init random input vector
random_vector = np.random.rand(500, 1)

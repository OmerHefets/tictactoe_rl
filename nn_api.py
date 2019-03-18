import random
import numpy as np


class NeuralNet:
    final_weights = {}

    def __init__(self, layers):
        self.layers = layers

    @staticmethod
    def f(x):
        return 1 / (1 + np.exp(-x))

    def init_random_weights(self):
        for i in range(len(self.layers)-1):
            # each matrix is the size of [l_1][l_0 + 1], (+1 because of the bias)
            random_weights = np.random.rand(self.layers[i+1], self.layers[i]+1)
            random_weights -= 0.5
            random_weights *= 2
            self.final_weights[i] = random_weights

    def vectorized_ff(self, x_vector, add_bias_to_vector):
        weights = self.final_weights
        vector = x_vector
        z = {}
        h = {}
        if add_bias_to_vector:
            vector = np.vstack((1, vector))
        for i in range(len(self.layers)-1):
            if not i == 0:
                vector = np.vstack((1, h[i]))
            z[i] = np.dot(weights[i], vector)
            h[i+1] = self.f(z[i])
        return h[len(self.layers)-1]


# init net
nn_layers = [500, 100, 9]
nn = NeuralNet(nn_layers)
nn.init_random_weights()


# init random input vector
random_vector = np.random.rand(500, 1)
print(nn.vectorized_ff(random_vector, add_bias_to_vector=True))

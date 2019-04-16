import random
import numpy as np


# val 0-8
def change1d_to_2d(val, edge):
    row = int(val / edge)
    column = val % edge
    return row, column


class NeuralNet:
    weights = {}
    bias = {}

    def __init__(self, layers, existing_weights):
        self.layers = layers
        self.nn_length = len(layers)
        self.grid_permutations = []
        self.permutations([], 1, 9)
        if existing_weights:
            self.load_weights()
        else:
            self.init_random_weights(is_rand=True)

    @staticmethod
    def sigma(x):
        return 1 / (1 + np.exp(-x))

    def sigma_der(self, x):
        return self.sigma(x) * (1 - self.sigma(x))

    def get_nn_value(self, para):
        if para == "permutations":
            return self.grid_permutations
        elif para == "layers":
            return self.layers
        elif para == "weights":
            return self.weights
        elif para == "bias":
            return self.bias
        else:
            exit("ERROR, NO SUCH NN VALUE")

    def init_random_weights(self, is_rand):
        for i in range(1, self.nn_length):
            if not is_rand:
                np.random.seed(42)
            # each weights is the size of [l_1][l_0]
            random_weights = np.random.rand(self.layers[i], self.layers[i-1])
            random_weights = (random_weights - 0.5) * 2
            self.weights[i] = random_weights
            # each bias is the size of [l_1][1]
            if not is_rand:
                np.random.seed(43)
            random_bias = np.random.rand(self.layers[i], 1)
            random_bias = (random_bias - 0.5) * 2
            self.bias[i] = random_bias

    def save_weights(self):
        for i in range(1, self.nn_length):
            weights_filename = "weights" + str(i) + ".csv"
            np.savetxt(weights_filename, self.weights[i], delimiter=",")
            bias_filename = "bias" + str(i) + ".csv"
            np.savetxt(bias_filename, self.bias[i], delimiter=",")

    def load_weights(self):
        for i in range(1, self.nn_length):
            weights_filename = "weights" + str(i) + ".csv"
            self.weights[i] = np.genfromtxt(weights_filename, delimiter=",")
            bias_filename = "bias" + str(i) + ".csv"
            self.bias[i] = np.genfromtxt(bias_filename, delimiter=",")
            # reshaping the bias for (n, 1) instead of (n,)
            self.bias[i] = np.reshape(self.bias[i], (len(self.bias[i]), 1))

    # Recursive function for defining array of (2^n - 1 ) arrays of (n * n) grid permutations
    def permutations(self, arr, index, MAX_VAL):
        if index > MAX_VAL:
            return
        local_array = arr[:]
        local_array.append(index)
        self.grid_permutations.append(local_array)
        self.permutations(arr[:], index+1, MAX_VAL)
        self.permutations(local_array, index+1, MAX_VAL)

    def vectorized_ff(self, x_vector):
        z = {}
        h = {1: x_vector}
        vector = x_vector
        for layer in range(1, self.nn_length):
            # if it's not the first layer
            if layer > 1:
                vector = h[layer]
            z[layer + 1] = np.dot(self.weights[layer], vector) + self.bias[layer]
            h[layer + 1] = self.sigma(z[layer + 1])
        return h, z

    def sgd_backpropagation(self, x_vector, y_vector, alpha):
        weights_derivative = {}
        bias_derivative = {}
        delta = {}
        h, z = self.vectorized_ff(x_vector)
        for layer in range(self.nn_length, 1, -1):
            if layer == self.nn_length:
                delta[self.nn_length] = -1 * (y_vector - h[self.nn_length]) * self.sigma_der(z[self.nn_length])
            else:
                delta[layer] = np.dot(np.transpose(self.weights[layer]), delta[layer + 1]) * self.sigma_der(z[layer])
        for layer in range(1, self.nn_length):
            weights_derivative[layer] = np.dot(delta[layer + 1], np.transpose(h[layer]))
            bias_derivative[layer] = delta[layer + 1]
        for layer in range(1, self.nn_length):
            self.weights[layer] -= alpha * weights_derivative[layer]
            self.bias[layer] -= alpha * bias_derivative[layer]


# init net
"""
nn_layers = [500, 100, 9]
nn = NeuralNet(nn_layers)
nn.init_random_weights(is_rand=False)
random_vector = np.random.rand(500, 1)
h, z = nn.vectorized_ff(random_vector)

y_vec = h[3]
y_vec[5] = 0

print(nn.bias[1])
nn.sgd_backpropagation(random_vector, y_vec, alpha=0.1)
print(nn.bias[1])
"""

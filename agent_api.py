import random
import numpy as np
import grid_api as g
import nn_api as nn


class Agent:

    def __init__(self):
        self.wins = 0
        self.losses = 0

    @staticmethod
    def get_grid_input(grid, permutations):
        # Reset input array
        h_1 = []
        for array in permutations:
            local_sum = 0
            for val in array:
                # (val - 1) since the recursive function's range is 1-9
                row, column = nn.change1d_to_2d(val-1, 3)
                local_sum += grid[row][column]
            h_1.append(local_sum)
        h_1 = np.reshape(h_1, (-1, 1))
        return h_1

    def action_pipeline(self, grid, neural_net):
        input_vector = self.get_grid_input(grid.get_grid(), neural_net.get_net_value(neural_net, "permutations"))
        print(input_vector)


a = Agent
test_grid = g.Grid(3)
test_nn = nn.NeuralNet

a.action_pipeline(a, test_grid, test_nn)

import random
import numpy as np
#import grid_api as g
import nn_api as nn


class Agent:

    grid_current_vals = 0

    def __init__(self):
        self.wins = 0
        self.losses = 0
        # define NN for 3 * 3 tic-tac-toe grid
        self.neural_net = nn.NeuralNet([511, 100, 9])
        self.neural_net.init_random_weights(is_rand=True)

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

    def agent_location(self, grid):
        input_vector = self.get_grid_input(grid.get_grid(), self.neural_net.get_nn_value("permutations"))
        h_vector, z_vector = self.neural_net.vectorized_ff(input_vector)
        self.grid_current_vals = h_vector[self.neural_net.nn_length]
        location = np.argmax(self.grid_current_vals)
        return location

    # for the full square option, backpropagate with all values equal, except the selected (MAX val) as 0
    def full_square(self, filled_location, grid, alpha):
        input_vector = self.get_grid_input(grid.get_grid(), self.neural_net.get_nn_value("permutations"))
        y_vector = self.grid_current_vals
        y_vector[filled_location] = 0
        self.neural_net.sgd_backpropagation(input_vector, y_vector, alpha=alpha)

#a = Agent()
#test_grid = g.Grid(3)

#a.action_pipeline(test_grid)

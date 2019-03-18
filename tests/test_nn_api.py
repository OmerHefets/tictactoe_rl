from nn_api import NeuralNet
import pytest
import numpy as np


@pytest.mark.parametrize("test_input,expected", [
    ([500, 100, 9], ((100, 501), (9, 101))),
    ([30, 30, 1], ((30, 31), (1, 31))),
    ([10, 15, 30], ((15, 11), (30, 16)))

])
def test_init_random_weights(test_input, expected):
    nn = NeuralNet(test_input)
    nn.init_random_weights()
    for i in range(len(test_input)-1):
        weights = nn.final_weights[i]
        assert np.shape(weights) == expected[i]

from nn_api import NeuralNet
import pytest
import numpy as np


@pytest.mark.parametrize("test_input,expected", [
    ([500, 100, 9], ((100, 500), (9, 100))),
    ([30, 30, 1], ((30, 30), (1, 30))),
    ([10, 15, 30], ((15, 10), (30, 15)))

])
def test_init_random_weights(test_input, expected):
    nn = NeuralNet(test_input)
    nn.init_random_weights()
    for i in range(len(test_input)-1):
        weights = nn.weights[i]
        assert np.shape(weights) == expected[i]

from nn_api import NeuralNet
import pytest
import numpy as np


@pytest.mark.parametrize("test_input,expected", [
    ([500, 100, 9], ((100, 500), (9, 100), (100, 1), (9, 1))),
    ([30, 30, 1], ((30, 30), (1, 30), (30, 1), (1, 1))),
    ([10, 15, 30], ((15, 10), (30, 15), (15, 1), (30, 1)))

])
def test_init_random_weights(test_input, expected):
    nn = NeuralNet(test_input)
    nn.init_random_weights(rand=True)
    expected_count = 0
    # test weights
    for i in range(1, len(test_input)):
        weights = nn.weights[i]
        assert np.shape(weights) == expected[expected_count]
        expected_count += 1
    # test biases
    for i in range(1, len(test_input)):
        biases = nn.bias[i]
        assert np.shape(biases) == expected[expected_count]
        expected_count += 1

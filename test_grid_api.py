from grid_api import Grid
import pytest

g = Grid(3)


@pytest.mark.parametrize("test_input,expected", [
    # diagonal
    ([0, 1, 0, 1, 0, 1, 0, 1, -1], "o_player"),
    # O 1st row
    ([0, 0, 0, -1, -1, -1, 1, 1, -1], "o_player"),
    # O 1st column
    ([-1, -1, 0, -1, 0, 1, -1, 1, 0], "no_winner"),
    # X 1st row
    ([1, 1, 1, -1, -1, -1, 0, 0, -1], "x_player"),
    # X 2nd row
    ([1, 0, 0, 1, 1, 1, 0, 0, -1], "x_player"),
    # empty board
    ([-1, -1, -1, -1, -1, -1, -1, -1, -1], "no_winner"),
    # X 3rd column
    ([-1, 0, 1, -1, -1, 1, -1, 0, 1], "x_player"),
])
def test_winner(test_input, expected):
    g.set_grid(test_input)
    assert g.find_a_winner() == expected

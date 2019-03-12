from grid_api import Grid
import pytest
import mock

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
def test_find_a_winner(test_input, expected):
    g.set_grid(test_input)
    assert g.find_a_winner() == expected


@pytest.mark.parametrize("test_input,expected", [
    (0, (0, 0)),
    (3, (1, 0)),
    (5, (1, 2)),
    (6, (2, 0)),
    (8, (2, 2))
])
def test_change1d_to_2d(test_input, expected):
    assert g.change1d_to_2d(test_input) == expected


# test_input = [grid, user_location]
@pytest.mark.parametrize("test_input,expected", [
    (([0, 1, 0, 1, 0, 1, 0, 1, -1], 9), True),
    (([0, 0, 0, -1, -1, -1, 1, 1, -1], 1), False),
    (([-1, -1, 0, -1, 0, 1, -1, 1, 0], 1), True),
    (([1, 1, 1, -1, 1, 0, 0, 0, -1], 4), True),
    (([1, 0, 0, 1, 1, 1, 0, 0, -1], 7), False),
    (([-1, -1, -1, -1, -1, -1, -1, -1, -1], 2), True),
    (([-1, 0, 1, -1, -1, 1, -1, 0, 1], 2), False)
])
def test_choose_location(test_input, expected, monkeypatch):
    g.set_grid(test_input[0])
    monkeypatch.setattr('builtins.input', lambda x: test_input[1])
    assert g.choose_location('x', 'human') == expected


@pytest.mark.parametrize("test_input,expected", [
    ([0, 1, 0, 1, 0, 1, 0, 1, -1], 3),
    ([0, 0, -1, -1, -1, -1, 1, 1, -1], -3),
    ([1, 1, 0, -1, 0, 1, -1, 1, 0], 2)
])
def test_sum_grid(test_input, expected):
    g.set_grid(test_input)
    assert g.sum_grid() == expected

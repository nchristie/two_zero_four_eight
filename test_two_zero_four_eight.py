from two_zero_four_eight import FourByFourGrid, shift_zeroes, left_move_row
import pytest

left = "A"
right = "D"
up = "W"
down = "S"


KEY = {"A": "left", "D": "right", "W": "up", "S": "down"}


@pytest.mark.parametrize(
    "row, expected",
    [
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([2, 0, 0, 0], [2, 0, 0, 0]),
        ([0, 0, 0, 2], [2, 0, 0, 0]),
        ([2, 2, 0, 0], [4, 0, 0, 0]),
        ([2, 0, 2, 0], [4, 0, 0, 0]),
        ([0, 0, 2, 2], [4, 0, 0, 0]),
        ([0, 2, 2, 2], [4, 2, 0, 0]),
        ([2, 2, 2, 2], [4, 4, 0, 0]),
    ],
)
def test_left_move_row(row, expected):
    assert expected == left_move_row(row)


@pytest.mark.parametrize(
    "move, start_grid, expected_result",
    [
        (
            left,
            [[2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 2]],
            [[2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0]],
        ),
        (
            left,
            [[0, 0, 0, 0], [0, 0, 0, 2], [0, 2, 8, 2], [0, 0, 0, 16]],
            [[0, 0, 0, 0], [2, 0, 0, 0], [2, 8, 2, 0], [16, 0, 0, 0]],
        ),
        (
            left,
            [[0, 2, 0, 8], [0, 0, 0, 8], [0, 0, 4, 8], [0, 0, 2, 4]],
            [[2, 8, 0, 0], [8, 0, 0, 0], [4, 8, 0, 0], [2, 4, 0, 0]],
        ),
        (
            right,
            [[8, 0, 2, 0], [8, 0, 0, 0], [8, 4, 0, 0], [4, 2, 0, 0]],
            [[0, 0, 8, 2], [0, 0, 0, 8], [0, 0, 8, 4], [0, 0, 4, 2]],
        ),
        (
            right,
            [[2, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
            [[0, 0, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
        ),
        (
            right,
            [[2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 2,]],
            [[0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 4],],
        ),
        (
            down,
            [[2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 2]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 2]],
        ),
    ],
)
def test_move(start_grid, move, expected_result):
    # GIVEN
    grid = FourByFourGrid()
    grid.grid = start_grid

    # WHEN
    grid.make_move(move)
    expected_result = expected_result
    # THEN
    assert expected_result == grid.grid, KEY[move]


def test_transpose_grid():
    # GIVEN
    grid = FourByFourGrid()
    grid.grid = [
        [2, 0, 0, 0,],
        [0, 0, 0, 0,],
        [2, 0, 0, 0,],
        [2, 0, 0, 2,],
    ]

    # WHEN
    grid.transpose()
    expected_result = [
        [2, 0, 2, 2,],
        [0, 0, 0, 0,],
        [0, 0, 0, 0,],
        [0, 0, 0, 2,],
    ]

    # THEN
    assert expected_result == grid.grid


@pytest.mark.parametrize(
    "row, expected", [([0, 2, 0, 8], [2, 8, 0, 0]), ([2, 2, 0, 2], [2, 2, 2, 0])]
)
def test_shift_zeroes(row, expected):
    # WHEN
    actual = shift_zeroes(row)

    # THEN
    assert expected == actual

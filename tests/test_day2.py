import pytest
from solutions.day2.part1 import solve as solve_part1
from solutions.day2.part2 import solve as solve_part2

# Test data
EXAMPLE_INPUT = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

def test_part1_example():
    assert solve_part1(EXAMPLE_INPUT) == 2

def test_part2_example():
    assert solve_part2(EXAMPLE_INPUT) == 4
    
import pytest
from solutions.day1.part1 import solve as solve_part1
from solutions.day1.part2 import solve as solve_part2

# Test data
EXAMPLE_INPUT = [[3, 4, 2, 1, 3, 3],[4, 3, 5, 3, 9, 3]]

def test_part1_example():
    assert solve_part1(EXAMPLE_INPUT) == 11

def test_part2_example():
    assert solve_part2(EXAMPLE_INPUT) == 31
    
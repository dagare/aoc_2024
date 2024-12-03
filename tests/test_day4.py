import pytest
from solutions.day4.solutions import solve_part1 as solve_part1
from solutions.day4.solutions import solve_part2 as solve_part2

# Test data
EXAMPLE_INPUT = 'mul(44,46)'

def test_part1_example():
    assert solve_part1(EXAMPLE_INPUT) == 2024

def test_part2_example():
    assert solve_part2(EXAMPLE_INPUT) == 2024
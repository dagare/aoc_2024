import pytest
from solutions.day0.part1 import solve as solve_part1
from solutions.day0.part2 import solve as solve_part2

# Test data
EXAMPLE_INPUT = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263"

def test_part1_example():
    assert solve_part1(EXAMPLE_INPUT) == 123

def test_part2_example():
    assert solve_part2(EXAMPLE_INPUT) == 898

@pytest.mark.parametrize(
    "data, expected",
    [
        ("100\n100\n100\n100", 123),  # Edge case: no increase
        ("199\n200\n208", 123),       # Minimal example
    ],
)
def test_part1_edge_cases(data, expected):
    assert solve_part1(data) == expected

@pytest.mark.parametrize(
    "data, expected",
    [
        ("100\n100\n100\n100", 898),  # Edge case: no sliding window increase
        ("199\n200\n208", 898),       # Too few measurements for sliding window
    ],
)
def test_part2_edge_cases(data, expected):
    assert solve_part2(data) == expected
import pytest
import solutions.day2_v2.solutions 

# Test data
EXAMPLE_INPUT = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

CORNER_CASES = [
    [31, 29, 31, 34, 35, 38, 41, 42],
    [29, 26, 27, 29, 31, 34],
    [86, 87, 86, 84, 81]
]

def test_part1_example():
    assert solutions.day2_v2.solutions.solve_part1(EXAMPLE_INPUT) == 2

def test_part2_example():
    (no_of_safe, unsafe_indexes, unsafe_reports) = solutions.day2_v2.solutions.solve_part2(EXAMPLE_INPUT)
    assert no_of_safe == 4

def test_part2_corner_cases_v1():
    (no_of_safe, unsafe_indexes, unsafe_reports) = solutions.day2_v2.solutions.solve_part2_v1(CORNER_CASES)
    assert no_of_safe == 3

def test_part2_corner_cases_v2():
    (no_of_safe, unsafe_indexes, unsafe_reports) = solutions.day2_v2.solutions.solve_part2_v2(CORNER_CASES)
    assert no_of_safe == 3
    
import pytest
from solutions.day4.utils import int_to_char as int_to_char
from solutions.day4.utils import char_to_int as char_to_int
from solutions.day4.solutions import lines_to_array as lines_to_array
from solutions.day4.solutions import solve_part1 as solve_part1
from solutions.day4.solutions import solve_part2 as solve_part2

# Test data
EXAMPLE_INPUT = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX'
]

EXAMPLE_INPUT_2 = [
    'XMASM',
    'MSAMX',
    'AMAMM',
    'SAAMA',
    'SSMMS'
]

def test_convert_example():
    array = lines_to_array(EXAMPLE_INPUT_2)
    
    char_array = int_to_char(array)
    int_array = char_to_int(char_array)

def test_part1_example():
    array = lines_to_array(EXAMPLE_INPUT)
    assert solve_part1(array) == 18

def test_part2_example():
    array = lines_to_array(EXAMPLE_INPUT)
    assert solve_part2(array) == 2024
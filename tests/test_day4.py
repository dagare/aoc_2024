import pytest
from solutions.day4.solutions import solve_part1 as solve_part1
from solutions.day4.solutions import solve_part2 as solve_part2
from solutions.day4.solutions import lines_to_array as lines_to_array

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

EXAMPLE_INPUT_3 = [
'.M.S......',
'..A..MSMS.',
'.M.S.MAA..',
'..A.ASMSM.',
'.M.S.M....',
'..........',
'S.S.S.S.S.',
'.A.A.A.A..',
'M.M.M.M.M.',
'..........',
]

def test_part1_example():
    array = lines_to_array(EXAMPLE_INPUT)
    assert solve_part1(array) == 18

def test_part2_example():
    array = lines_to_array(EXAMPLE_INPUT_3)
    assert solve_part2(array) == 9
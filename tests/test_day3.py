import pytest
from solutions.day3.solutions import solve_part1 as solve_part1
from solutions.day3.solutions import solve_part2 as solve_part2

# Test data
EXAMPLE_INPUT_2024 = 'mul(44,46)'
EXAMPLE_INPUT_492 = 'mul(123,4)'

EXAMPLE_INPUT_INVALID = [
    'mul(4*',
    'mul(6,9!',
    '?(12,34)',
    'mul ( 2 , 4 )'
]

EXAMPLE_INPUT_161 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(8, 3) mul(2,x2)'

EXAMPLE_INPUT_DO_DONT = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))mul(8, 3) mul(2,x2)"

def test_part1_example():
    assert solve_part1(EXAMPLE_INPUT_2024) == 2024
    assert solve_part1(EXAMPLE_INPUT_492) == 492
    assert solve_part1("".join(EXAMPLE_INPUT_INVALID)) == 0
    assert solve_part1(EXAMPLE_INPUT_161) == 161
    assert solve_part1(EXAMPLE_INPUT_DO_DONT) == 161


def test_part2_example():
    assert solve_part2(EXAMPLE_INPUT_2024) == 2024
    assert solve_part2(EXAMPLE_INPUT_492) == 492
    assert solve_part2("".join(EXAMPLE_INPUT_INVALID)) == 0
    assert solve_part2(EXAMPLE_INPUT_161) == 161
    assert solve_part2(EXAMPLE_INPUT_DO_DONT) == 48
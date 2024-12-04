import numpy as np
from scipy.signal import convolve2d

def char_to_num(c):
    if c == 'X':
        return 1
    elif c == 'M':
        return 2
    elif c == 'A':
        return 3
    elif c == 'S':
        return 4
    elif c == '.':
        return 0
    
    print(f'Value {c} -> 0')
    return 0

def parse_file(file_path):
    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    
    return lines

def lines_to_array(lines):
    data = []

    for line in lines:
        # print(f'line:{line.strip()}')
        data.append(list(line.strip()))

    data_as_int = []
    for row in data:

        int_row = []
        for char in row:
            int_row.append(char_to_num(char))

        data_as_int.append(int_row)

    return np.array(data_as_int)

# patterns = {
#     'horizontal': np.array([[1, 2, 3, 4]]),
#     'horizontal_reverse': np.array([[4, 3, 2, 1]]),
#     'vertical': np.array([[1], [2], [3], [4]]),
#     'vertical_reverse': np.array([[4], [3], [2], [1]]),
#     'diagonal_down_right': np.diag([1, 2, 3, 4]),
#     'diagonal_down_right_reverse': np.diag([4, 3, 2, 1]),
#     'diagonal_down_left': np.flipud(np.diag([1, 2, 3, 4])),
#     'diagonal_down_left_reverse': np.flipud(np.diag([4, 3, 2, 1]))
# }

lr = list([1, 2, 3, 4])
rl = list([4, 3, 2, 1])

patterns = {
    'horizontal': np.array([lr]),
    'horizontal_reverse': np.array([rl]),
    'vertical': np.array([lr]).transpose(),
    'vertical_reverse': np.array([rl]).transpose(),
    'diagonal_down_right': np.diag(lr),
    'diagonal_down_right_reverse': np.diag(rl),
    'diagonal_down_left': np.flipud(np.diag(lr)),
    'diagonal_down_left_reverse': np.flipud(np.diag(rl))
}

ones = list([1, 1, 1, 1])

diagonal_kernel = {
    'horizontal': np.array([ones]),
    'horizontal_reverse': np.array([ones]),
    'vertical': np.array([ones]).transpose(),
    'vertical_reverse': np.array([ones]).transpose(),
    'diagonal_down_right': np.diag(ones),
    'diagonal_down_right_reverse': np.diag(ones),
    'diagonal_down_left': np.flipud(np.diag(ones)),
    'diagonal_down_left_reverse': np.flipud(np.diag(ones))
}

the_x = [
    [2, 0, 4],
    [0, 3, 0],
    [2, 0, 4]]


xmas_kernels = {
    'deg_0': np.array(the_x),
    '90deg': np.rot90(the_x),
    '180deg': np.rot90(the_x, k=2),
    '270deg': np.rot90(the_x, k=3),
}

xmas_boolean_kernel = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

def all_is_same(sub_region, pattern, match, direction):
    r, c = match
    pr, pc = pattern.shape  # Get pattern dimensions
            
    if sub_region.shape != pattern.shape:
        return False

    # Diagonal checks
    if direction == 'diagonal_down_right' or direction == 'diagonal_down_right_reverse':
        diag_match = np.all(np.diagonal(sub_region) == np.diagonal(pattern))
        return diag_match
    
    elif direction == 'diagonal_down_left' or direction == 'diagonal_down_left_reverse':
        # Top-right to bottom-left diagonal match
        anti_diag_match = np.all(np.diagonal(np.fliplr(sub_region)) == np.diagonal(np.fliplr(pattern)))
        return anti_diag_match
    
    # Horizontal or vertical match
    return np.array_equal(sub_region, pattern)

def all_is_same_for_x(sub_region, pattern, match, direction):
    r, c = match
    pr, pc = pattern.shape  # Get pattern dimensions
            
    if sub_region.shape != pattern.shape:
        return False

    diag_match = np.all(np.diagonal(sub_region) == np.diagonal(pattern))
    
    anti_diag_match = np.all(np.diagonal(np.fliplr(sub_region)) == np.diagonal(np.fliplr(pattern)))
    
    return diag_match and anti_diag_match

def solve_part1(array, print_debug=False):
    occurrences = 0
    all_matches = 0

    for direction, pattern in patterns.items():
        conv_result = convolve2d(array, pattern, mode='valid')
        # pattern_sum = np.sum(pattern**2)
        pattern_sum_2 = convolve2d(pattern, pattern, mode='valid')
        pattern_sum_2_ = np.sum(convolve2d(pattern, pattern, mode='valid'))
        matches = np.argwhere(conv_result == pattern_sum_2_)
        all_matches += len(matches)

        sum = np.sum(conv_result == pattern_sum_2_)
        # occurrences += int(sum)

        highlighted_array = np.full_like(array, 0)
        for match in matches:
            r, c = match
            pr, pc = pattern.shape  # Get pattern dimensions

            # Extract sub-region
            sub_region = array[r:r+pr, c:c+pc]
            
            if all_is_same(sub_region, pattern, match, direction):
                # Convolve with the pattern
                convolved_value = np.sum(sub_region ** diagonal_kernel[direction])
                
                # Update highlighted array (diagonal elements)
                highlighted_array[r:r+pr, c:c+pc] = convolved_value
                # highlighted_array[r:r+pr, c:c+pc] = array[r:r+pr, c:c+pc]
                occurrences += 1

        if print_debug: print(f'direction:{direction} pattern:\n{pattern}')
        if print_debug: print(f'highlighted_array:\n{highlighted_array}')
    
    if print_debug: print(f'occurrences:{occurrences} all_matches:{all_matches}')

    return occurrences

def solve_part2(array, print_debug=False):
    occurrences = 0

    for direction, pattern in xmas_kernels.items():
        conv_result = convolve2d(array, pattern, mode='valid')
        # pattern_sum = np.sum(pattern**2)
        pattern_sum_2 = convolve2d(pattern, pattern, mode='valid')
        pattern_sum_2_ = np.sum(convolve2d(pattern, pattern, mode='valid'))
        matches = np.argwhere(conv_result == pattern_sum_2_)

        sum = np.sum(conv_result == pattern_sum_2_)

        highlighted_array = np.full_like(array, 0)
        for match in matches:
            r, c = match
            pr, pc = pattern.shape  # Get pattern dimensions

            # Extract sub-region
            sub_region = array[r:r+pr, c:c+pc]
            
            if all_is_same_for_x(sub_region, pattern, match, direction):
                # Convolve with the pattern
                convolved_value = np.sum(sub_region ** xmas_boolean_kernel)
                
                # Update highlighted array (diagonal elements)
                highlighted_array[r:r+pr, c:c+pc] = convolved_value
                # highlighted_array[r:r+pr, c:c+pc] = array[r:r+pr, c:c+pc]
                occurrences += 1

        if print_debug: print(f'direction:{direction} pattern:\n{pattern}')
        if print_debug: print(f'highlighted_array:\n{highlighted_array}')
    
    if print_debug: print(f'occurrences:{occurrences}')

    return occurrences


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

def main():
   


    print("\nPart 1 (example):", solve_part1(lines_to_array(EXAMPLE_INPUT_2)))
    print("\nPart 1 (example one):", solve_part1(lines_to_array(EXAMPLE_INPUT)))

    input_file = "solutions/day4/input.txt"
    lines = parse_file(input_file)
    array = lines_to_array(lines)

    print("\nPart 1:", solve_part1(array))

    print("\nPart 2 (example):", solve_part2(lines_to_array(EXAMPLE_INPUT_3)))

    print("\nPart 2:", solve_part2(array))

if __name__ == "__main__":
    main()
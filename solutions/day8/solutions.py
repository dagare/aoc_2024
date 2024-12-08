import numpy as np

EXAMPLE_INPUT = [
'............',
'........0...',
'.....0......',
'.......0....',
'....0.......',
'......A.....',
'............',
'............',
'........A...',
'.........A..',
'............',
'............'
]

def parse_file(file_path):

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    
    return lines

class Node:
    def __init__(self, frequency):
        self.antinode = False
        self.frequency = frequency
        self.is_antenna = frequency != '.'

    def set_reflection(self):
        self.antinode = True

    def __repr__(self):
        if self.is_antenna:
            return self.frequency

        if self.antinode:
            return '#'

        return '.'

def parse_lines(lines):
    
    matrix = np.empty((len(lines), len(lines[0])), dtype=object) 
    for (i, line) in enumerate(lines):
        for (j, frequency) in enumerate(list(line)):
            matrix[i, j] = Node(frequency) 
    return matrix

def solve_part1(map, debug=False):
    sum = 0
    return sum

def solve_part2(map, debug=False):
    sum = 0
    return sum

def main():
   

    map = parse_lines(EXAMPLE_INPUT)
    print(map)
    p1 = solve_part1(map, True)
    print(f'Part 1 (example): {p1} Correct: {p1==3749}')
    p2 = solve_part2(map, True)
    print(f'Part 2 (example): {p2} Correct: {p2==11387}')

    input_file = "solutions/day8/input.txt"
    lines = parse_file(input_file)
    map = parse_lines(lines)

    print("\nPart 1:", solve_part1(map))
    print("\nPart 2:", solve_part2(map))

if __name__ == "__main__":
    main()
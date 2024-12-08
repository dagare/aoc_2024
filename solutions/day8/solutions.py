import numpy as np
import itertools

SIMPLE_INPUT = [
'.......',
'.......',
'..1....',
'....1..',
'..2.1..',
'.2.....',
'.......',
]

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

class Map:
    def __init__(self, lines):
        self.frequency_locations = dict()

        self.map = np.empty((len(lines), len(lines[0])), dtype=object) 
        for (i, line) in enumerate(lines):
            for (j, frequency) in enumerate(list(line)):
                node = Node(frequency) 

                self.map[i, j] = node

                if node.is_antenna:
                    if not frequency in self.frequency_locations:
                        self.frequency_locations[frequency] = []
                    self.frequency_locations[frequency].append((i,j))
    
        self.rows, self.cols = self.map.shape

    def find_reflections(self):

        for frequency, locations in self.frequency_locations.items():
            
            for a, b in itertools.combinations(locations, 2):
                d = (a[0] - b[0], a[1] - b[1])
                (i, j) = (a[0] + d[0], a[1] + d[1])
                if self.is_index_in_matrix(i,j):
                    self.map[i,j].set_reflection()

                d = (b[0] - a[0], b[1] - a[1])
                (i, j) = (b[0] + d[0], b[1] + d[1])
                if self.is_index_in_matrix(i,j):
                    self.map[i,j].set_reflection()

    def is_index_in_matrix(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols
    
    def sum_antinodes(self):
        sum = 0
        for element in self.map.flat:
            if element.antinode:
                sum += 1

        return sum


    def __repr__(self):
        return f'{self.map}'



def solve_part1(map, debug=False):

    map.find_reflections()

    return map.sum_antinodes()

def solve_part2(map, debug=False):
    sum = 0
    return sum

def main():
    map = Map(SIMPLE_INPUT)
    print(f'Before:\n{map}')
    p1 = solve_part1(map, True)
    print(f'After:\n{map}')

    map = Map(EXAMPLE_INPUT)
    print(f'Before:\n{map}')
    p1 = solve_part1(map, True)
    print(f'After:\n{map}')
    print(f'Part 1 (example): {p1} Correct: {p1==14}')
    p2 = solve_part2(map, True)
    print(f'Part 2 (example): {p2} Correct: {p2==11387}')

    input_file = "solutions/day8/input.txt"
    lines = parse_file(input_file)
    map = Map(lines)

    print("\nPart 1:", solve_part1(map))
    print("\nPart 2:", solve_part2(map))

if __name__ == "__main__":
    main()
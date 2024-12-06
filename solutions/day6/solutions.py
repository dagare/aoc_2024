import numpy as np

SIMPLE_INPUT_1 = [
'.#..',
'....',
'.^..',
'....'
]

SIMPLE_INPUT_2 = [
'.#..',
'...#',
'.^..',
'....'
]

EXAMPLE_INPUT = [
'....#.....',
'.........#',
'..........',
'..#.......',
'.......#..',
'..........',
'.#..^.....',
'........#.',
'#.........',
'......#...'
]

def parse_file(file_path):

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    
    return lines


def parse_lines(lines):
    
    map = []

    for line in lines:
        if '.' in line:
            map.append(list(line.strip()))

    return map

class Guard:
    def __init__(self, i, j, dir):
        self.pos = (i, j)
        self.dir = dir

class Map:
    def __init__(self, lines):
        self.map = []

        for line in lines:
            if '.' in line:
                self.map.append(list(line.strip()))

        self.array = np.array(self.map, dtype='<U1')

        self.map_size = (len(self.map), len(self.map[0]))

        a = 0
        b = a +1
        guard = self.find_guard()

        c = 0


    def find_guard(self):

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                if self.map[i][j] in '<>^v':
                    return Guard(i, j, self.map[i][j])

        return None
        
    def move_guard(self, guard): 

        next_position = None

        if guard.dir == '<':
            next_position = (guard.pos[0], guard.pos[1]-1)
        elif guard.dir == '>':
            next_position = (guard.pos[0], guard.pos[1]+1)
        elif guard.dir == '^':
            next_position = (guard.pos[0]-1, guard.pos[1])
        elif guard.dir == 'v':
            next_position = (guard.pos[0]+1, guard.pos[1])

        # is obstacle -> turn direction (not done)
        if self.map[next_position[0]][next_position[1]] == '#':
            if guard.dir == '<':
                guard.dir = '^'
            elif guard.dir == '>':
                guard.dir = 'v'
            elif guard.dir == '^':
                guard.dir = '>'
            elif guard.dir == 'v':
                guard.dir = '<'

            return (guard, False)

        # Set state to visited
        if self.map[next_position[0]][next_position[1]] == '.': 
            self.map[next_position[0]][next_position[1]] = 'x'
        # elif self.map[next_position[0]][next_position[1]] in '<>^v': 
        #     self.map[next_position[0]][next_position[1]] = 'x'

        guard.pos = next_position

        return (guard, self.is_at_end(guard))

    def is_at_end(self, guard):

        if guard.pos[0] == 0:
            return True
        elif guard.pos[0] == len(self.map[0])-1:
            return True
        elif guard.pos[1] == 0:
            return True
        elif guard.pos[1] == len(self.map[0])-1:
            return True
        
        return False

    def summarize_visited_cells(self):
        sum = 0
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                if self.map[i][j] == 'x':
                    sum += 1
                elif self.map[i][j] in '<>^v':
                    sum += 1
        return sum
                    


def solve_part1(map):
    guard = map.find_guard()
        
    (guard, is_done) = (guard, False)
    while not is_done:
        (guard, is_done) = map.move_guard(guard)

    return map.summarize_visited_cells()

def solve_part2(map):
    
    sum = 0

    return sum


def main():
    simple_map_1 = Map(SIMPLE_INPUT_1)
    p1 = solve_part1(simple_map_1)
    print(f'Part 1 (simple_1): {p1} Correct: {p1==4}')
    simple_map_2 = Map(SIMPLE_INPUT_2)
    p1 = solve_part1(simple_map_2)
    print(f'Part 1 (simple_2): {p1} Correct: {p1==5}')

    example_map = Map(EXAMPLE_INPUT)
    p1 = solve_part1(example_map)
    print(f'Part 1 (example): {p1} Correct: {p1==41}')
    p2 = solve_part2(example_map)
    print(f'Part 2 (example): {p2} Correct: {p2==6}')

    input_file = "solutions/day6/input.txt"
    lines = parse_file(input_file)
    map = Map(lines)

    print("\nPart 1:", solve_part1(map))
    print("\nPart 2:", solve_part2(map))

if __name__ == "__main__":
    main()
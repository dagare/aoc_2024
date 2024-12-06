import numpy as np
import copy

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

    def __eq__(self, other):
        if not isinstance(other, Guard):
            return NotImplemented
        return self.pos == other.pos and self.dir == other.dir

    def __repr__(self):
        return f"Guard(pos={self.pos}, dir={self.dir})"
    
class Map:
    def __init__(self, lines):
        self.map = []

        for line in lines:
            if '.' in line:
                self.map.append(list(line.strip()))

        # self.array = np.array(self.map, dtype='<U1')

        self.map_size = (len(self.map), len(self.map[0]))

        self.previous_guard_states = []


    def find_guard(self):

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                if self.map[i][j] in '<>^v':
                    return Guard(i, j, self.map[i][j])

        return None
        
    def move_guard(self, guard): 
        self.previous_guard_states.append(guard)

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
    
    def is_in_infinite_loop(self, guard):

        if guard in self.previous_guard_states:
            return True
        
        return False

    def summarize_visited_cells(self):
        sum = 0
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                if self.map[i][j] == 'x':
                    sum += 1
                # elif self.map[i][j] in '<>^v':
                #     sum += 1

        # just add one for the start position
        sum +=1 

        return sum
                    


def solve_part1(map):
    guard = map.find_guard()
        
    (guard, is_done) = (guard, False)
    while not is_done:
        (guard, is_done) = map.move_guard(guard)

    return map.summarize_visited_cells()

def solve_part2(lines):
    map = Map(lines)

        
    infinite_loop_cnt = 0
    infinite_loop_positions = []

    for i in range(map.map_size[0]):
        for j in range(map.map_size[1]):
            if map.map[i][j] == '.':
                temp_map = Map(lines)
                temp_map.map[i][j] = 'x'
                guard = temp_map.find_guard()
            
                (guard, is_done) = (guard, False)
                while not is_done:
                    (guard, is_done) = temp_map.move_guard(guard)
                    
                    if temp_map.is_in_infinite_loop(guard):
                        infinite_loop_positions.append((i, j))
                        infinite_loop_cnt += 1
                        break

    return infinite_loop_cnt


def main():
    simple_map_1 = Map(SIMPLE_INPUT_1)
    p11 = solve_part1(simple_map_1)
    print(f'Part 1 (simple_1): {p11} Correct: {p11==4}')
    simple_map_2 = Map(SIMPLE_INPUT_2)
    p12 = solve_part1(simple_map_2)
    print(f'Part 1 (simple_2): {p12} Correct: {p12==5}')

    example_map = Map(EXAMPLE_INPUT)
    p1 = solve_part1(example_map)
    print(f'Part 1 (example): {p1} Correct: {p1==41}')


    p21 = solve_part2(SIMPLE_INPUT_1)
    print(f'Part 2 (simple_1): {p21} Correct: {p21==0}')
    p22 = solve_part2(SIMPLE_INPUT_1)
    print(f'Part 2 (simple_2): {p22} Correct: {p22==0}')


    p2 = solve_part2(EXAMPLE_INPUT)
    print(f'Part 2 (example): {p2} Correct: {p2==6}')

    input_file = "solutions/day6/input.txt"
    lines = parse_file(input_file)
    map = Map(lines)

    print("\nPart 1:", solve_part1(map))
    print("\nPart 2:", solve_part2(lines))

if __name__ == "__main__":
    main()
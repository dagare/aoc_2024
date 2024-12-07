import numpy as np
from tqdm import tqdm
import copy
import os
import time

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

        self.m = len(self.map)
        self.n = len(self.map[0])

        self.previous_guard_states = []


    def find_guard(self):

        for i in range(self.m):
            for j in range(self.n):
                if self.map[i][j] in '<>^v':
                    return Guard(i, j, self.map[i][j])

        return None
        
    def move_guard(self, guard): 
        self.previous_guard_states.append(copy.deepcopy(guard))

        next_position = None

        # Find out where next position should be
        if guard.dir == '<':
            next_position = (guard.pos[0], guard.pos[1]-1)
        elif guard.dir == '>':
            next_position = (guard.pos[0], guard.pos[1]+1)
        elif guard.dir == '^':
            next_position = (guard.pos[0]-1, guard.pos[1])
        elif guard.dir == 'v':
            next_position = (guard.pos[0]+1, guard.pos[1])

        # next is obstacle -> turn direction (not done)
        if self.map[next_position[0]][next_position[1]] in '#@':
            # self.map[guard.pos[0]][guard.pos[1]] = '┼'
            

            if guard.dir == '<':
                guard.dir = '^'
                self.map[guard.pos[0]][guard.pos[1]] = '└'
            elif guard.dir == '>':
                guard.dir = 'v'
                self.map[guard.pos[0]][guard.pos[1]] = '┐'
            elif guard.dir == '^':
                guard.dir = '>'
                self.map[guard.pos[0]][guard.pos[1]] = '┌'
            elif guard.dir == 'v':
                guard.dir = '<'
                self.map[guard.pos[0]][guard.pos[1]] = '┘'

            return (guard, False)

        # Set state to visited
        if self.map[next_position[0]][next_position[1]] == '.': 
            if guard.dir in '<>':
                self.map[next_position[0]][next_position[1]] = '─'
            elif guard.dir in '^v':
                self.map[next_position[0]][next_position[1]] = '│'
        elif self.map[next_position[0]][next_position[1]] in '─│': 
            self.map[next_position[0]][next_position[1]] = '┼'

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
        for i in range(self.m):
            for j in range(self.n):
                if self.map[i][j] in 'x<>^v─│┼┌┘┐└':
                    sum += 1
                # elif self.map[i][j] in '<>^v':
                #     sum += 1

        # just add one for the start position
        # sum +=1 

        return sum
    
    def get_visited_cells_wo_start(self):
        visited_cells=[]
        for i in range(self.m):
            for j in range(self.n):
                if self.map[i][j] in 'x─│┼┌┘┐└':
                    visited_cells.append((i, j))

        return visited_cells
                
    def save_to_file(self, path):
        with open(path, 'w') as f:
            for line in self.map:
                f.write(f"{''.join(line)}\n")

def solve_part1(map):
    guard = map.find_guard()
        
    (guard, is_done) = (guard, False)
    while not is_done:
        (guard, is_done) = map.move_guard(guard)

    return map.summarize_visited_cells()

def solve_part2(lines, filename):
    solved_map = Map(lines)

    # Solve one first (to highligh visited areas)
    guard = solved_map.find_guard()
    (guard, is_done) = (guard, False)
    while not is_done:
        (guard, is_done) = solved_map.move_guard(guard)

    solved_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/solved_"+filename+".log"))
    # with open(filename, 'w') as f:
    #     for line in solved_map.map:
    #         f.write(f"{''.join(line)}\n")

    cells_to_try = solved_map.get_visited_cells_wo_start()

    infinite_loop_cnt = 0
    infinite_loop_positions = []

    start_time = time.time()

    total_iterations = len(cells_to_try)
    for (i, j) in cells_to_try:
        current_iter_start_time = time.time()
        temp_map = Map(lines)
        temp_map.map[i][j] = '@'
        guard = temp_map.find_guard()
    
        # (guard, is_done) = (guard, False)
        is_done = False
        is_infinite_loop = False
        while not is_done:
            (guard, is_done) = temp_map.move_guard(guard)
            
            if temp_map.is_in_infinite_loop(guard):
                infinite_loop_positions.append((i, j))
                infinite_loop_cnt += 1
                temp_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/"+filename+f'_(i,j):({i},{j})_{i*j}.log'))
                with open(os.path.join(os.path.dirname(__file__), "infinite_loops/"+filename+f'_infinite_loop_indexes.log'), 'a') as f:
                    f.write(f"{i},{j}\n")
                is_infinite_loop = True
                break

        iter_time = time.time() - current_iter_start_time
        total_time = time.time() - start_time
        print(f'(i,j):({i},{j}) \tinfinite_loop:{is_infinite_loop} \tinfinite_loop_cnt:{infinite_loop_cnt} \titer_time:{iter_time:.1f} \ttotal_time:{total_time:.1f}')

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


    p21 = solve_part2(SIMPLE_INPUT_1, "part2_simple1")
    print(f'Part 2 (simple_1): {p21} Correct: {p21==0}')
    p22 = solve_part2(SIMPLE_INPUT_2, "part2_simple2")
    print(f'Part 2 (simple_2): {p22} Correct: {p22==0}')


    p2 = solve_part2(EXAMPLE_INPUT, "part2_example")
    print(f'Part 2 (example): {p2} Correct: {p2==6}')

    input_file = "solutions/day6/input.txt"
    lines = parse_file(input_file)
    map = Map(lines)

    print("\nPart 1:", solve_part1(map))
    print("\nPart 2:", solve_part2(lines, "part2_real"))

if __name__ == "__main__":
    main()

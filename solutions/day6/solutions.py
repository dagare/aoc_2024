import numpy as np
from tqdm import tqdm
import copy
import os
import time
from pathlib import Path

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

    def turn(self):
        if self.dir == '<':
            self.dir = '^'
        elif self.dir == '>':
            self.dir = 'v'
        elif self.dir == '^':
            self.dir = '>'
        elif self.dir == 'v':
            self.dir = '<'

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
    Path(os.path.join(os.path.dirname(__file__), "debug/v1/infinite_loops")).mkdir(parents=True, exist_ok=True)

    solved_map = Map(lines)

    # Solve one first (to highligh visited areas)
    guard = solved_map.find_guard()
    (guard, is_done) = (guard, False)
    while not is_done:
        (guard, is_done) = solved_map.move_guard(guard)

    solved_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/v1/solved_"+filename+".log"))
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
                temp_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/v1/"+filename+f'_(i,j):({i},{j})_{i*j}.log'))
                with open(os.path.join(os.path.dirname(__file__), "debug/v1/infinite_loops/"+filename+f'_infinite_loop_indexes.log'), 'a') as f:
                    f.write(f"{i},{j}\n")
                is_infinite_loop = True
                break

        iter_time = time.time() - current_iter_start_time
        total_time = time.time() - start_time
        print(f'(i,j):({i},{j}) \tinfinite_loop:{is_infinite_loop} \tinfinite_loop_cnt:{infinite_loop_cnt} \titer_time:{iter_time:.1f} \ttotal_time:{total_time:.1f}')

    return infinite_loop_cnt

class EntryExit:
    def __init__(self, entry_dir, exit_dir):
        # in order [up, right, down, left]
        self.entry = [False, False, False, False]
        self.exit = [False, False, False, False]

        if entry_dir:
            self.entry[entry_dir] = True

        if exit_dir:
            self.exit[exit_dir] = True

    def set(self, entry_dir, exit_dir):
        # in order [up, right, down, left]
        if entry_dir:
            self.entry[entry_dir] = True
        self.exit[exit_dir] = True

    def entry_from(self, dir):
        if dir == "top":
            return self.entry[0]
        elif dir == "right":
            return self.entry[1]
        elif dir == "bottom":
            return self.entry[2]
        elif dir == "left":
            return self.entry[3]
        elif dir == "start_node":
            a=0
        
    def exit_from(self, dir):
        if dir == "top":
            return self.entry[0]
        elif dir == "right":
            return self.entry[1]
        elif dir == "bottom":
            return self.entry[2]
        elif dir == "left":
            return self.entry[3]

    def __eq__(self, other):
        if not isinstance(other, EntryExit):
            return NotImplemented
        return self.entry == other.entry and self.exit == other.exit
        

class Cell:
    def __init__(self, char):
        self.start = False
        self.barrier = False
        self.new_barrier = False
        self.edge = False

        # in order [up, right, down, left]
        self.entry_exits = []

        if char in '^>v<':
            self.start = True
            if char == '^':
                self.entry_exits.append(EntryExit(None, 0))
            elif char == '>':
                self.entry_exits.append(EntryExit(None, 1))
            elif char == 'v':
                self.entry_exits.append(EntryExit(None, 2))
            elif char == '<':
                self.entry_exits.append(EntryExit(None, 3))
        elif char == '#':
            self.barrier = True
        elif char == '.':
            self.empty = True

    def has_been_visited(self):
        if self.start:
            return True
        
        return (len(self.entry_exits)) > 0

    def set_to_barrier(self):
        self.new_barrier = True
        self.barrier = True

    def is_barrier(self):
        return self.new_barrier or self.barrier

    def set_to_visited(self, entry_exit):
        if entry_exit in self.entry_exits:
            # We're in a loop!!
            return False
        
        self.entry_exits.append(entry_exit)

        return True

    def __repr__(self):
        if self.start:
            if self.entry_exits[0].exit_from("top"):
                return '^'
            elif self.entry_exits[0].exit_from("bottom"):
                return 'v'
            elif self.entry_exits[0].exit_from("left"):
                return '<'
            elif self.entry_exits[0].exit_from("right"):
                return '>'
            else:
                '?'
        
        if self.new_barrier:
            return '@'
        
        if self.barrier:
            return '#'
        
        if self.edge:
            return 'Ø'
        
        if len(self.entry_exits) > 1:
            return '┼'
        
        if len(self.entry_exits):
            if self.entry_exits[0].entry_from("top"):
                if self.entry_exits[0].exit_from("bottom"): 
                    return '│'
                elif self.entry_exits[0].exit("left"): 
                    return '┘'
            elif self.entry_exits[0].entry_from("right"):
                if self.entry_exits[0].exit_from("left"): 
                    return '─'
                elif self.entry_exits[0].exit_from("top"): 
                    return '└'
            elif self.entry_exits[0].entry_from("bottom"):
                if self.entry_exits[0].exit_from("top"): 
                    return '│'
                elif self.entry_exits[0].exit_from("right"): 
                    return '┌'
            elif self.entry_exits[0].entry_from("left"):
                if self.entry_exits[0].exit_from("right"): 
                    return '─'
                elif self.entry_exits[0].exit_from("bottom"): 
                    return '┐'

        return '.'

class Map_v2:
    def __init__(self, lines):
        self.guard = None
        self.initial_guard = None

        self.map = np.empty((len(lines), len(lines[0])), dtype=object) 
        for (i, line) in enumerate(lines):
            for (j, state_char) in enumerate(list(line)):
                node = Cell(state_char) 
   
                self.map[i, j] = node
                if i == 0 or j == 0 or i >= len(lines)-1 or j >= len(list(line))-1:
                    self.map[i, j].edge = True 

                if state_char in '<>^v':
                    self.guard = Guard(i, j, state_char)
                    self.initial_guard = Guard(i, j, state_char)

        self.rows, self.cols = self.map.shape
                    
        
    def move_guard(self): 
        next_position = None
        entry_exit = None

        # Find out where next position should be
        if self.guard.dir == '<':
            next_position = (self.guard.pos[0], self.guard.pos[1]-1)
            entry_exit = EntryExit(1, 3)
        elif self.guard.dir == '>':
            next_position = (self.guard.pos[0], self.guard.pos[1]+1)
            entry_exit = EntryExit(3, 1)
        elif self.guard.dir == '^':
            next_position = (self.guard.pos[0]-1, self.guard.pos[1])
            entry_exit = EntryExit(2, 0)
        elif self.guard.dir == 'v':
            next_position = (self.guard.pos[0]+1, self.guard.pos[1])
            entry_exit = EntryExit(0, 2)

        # next is obstacle -> turn direction (not done)
        if self.map[next_position[0], next_position[1]].is_barrier():

            if self.guard.dir == '<':
                self.guard.turn()
                entry_exit = EntryExit(1, 0)
                next_position = (self.guard.pos[0]+1, self.guard.pos[1])
            elif self.guard.dir == '>':
                self.guard.turn()
                entry_exit = EntryExit(3, 2)
                next_position = (self.guard.pos[0]-1, self.guard.pos[1])
            elif self.guard.dir == '^':
                self.guard.turn()
                entry_exit = EntryExit(2, 1)
                next_position = (self.guard.pos[0], self.guard.pos[1]+1)
            elif self.guard.dir == 'v':
                self.guard.turn()
                entry_exit = EntryExit(0, 3)
                next_position = (self.guard.pos[0], self.guard.pos[1]-1)


        ok = self.map[self.guard.pos[0], self.guard.pos[1]].set_to_visited(entry_exit)

        in_a_infinate_loop = False
        if not ok:
            # We're in a infinite loop!!
            in_a_infinate_loop = True

        # Update guard position
        self.guard.pos = next_position

        return (self.is_at_end(), in_a_infinate_loop)

    def is_at_end(self):

        if self.guard.pos[0] == 0:
            return True
        elif self.guard.pos[0] == len(self.map[0])-1:
            return True
        elif self.guard.pos[1] == 0:
            return True
        elif self.guard.pos[1] == len(self.map[0])-1:
            return True
        
        return False
    
    def is_outside_bounds(self, i, j):

        if i < 0:
            return True
        elif i > self.rows-1:
            return True
        elif j < 0:
            return True
        elif j >  self.cols-1:
            return True
        
        return False
    
    def is_in_infinite_loop(self):

        if self.guard in self.previous_guard_states:
            return True
        
        return False

    def summarize_visited_cells(self):
        sum = 0
        for element in self.map.flat:
            if element.has_been_visited():
                sum += 1

        return sum
    
    def get_visited_cells_wo_start(self):
        visited_cells=[]
        # for i in range(self.m):
        #     for j in range(self.n):
        #         if self.map[i][j] in 'x─│┼┌┘┐└':
        #             visited_cells.append((i, j))
        for index, cell in np.ndenumerate(self.map):
            if cell.has_been_visited() and not cell.start:
                visited_cells.append(index)

        return visited_cells
                
    def save_to_file(self, path):
        with open(path, 'w') as f:
            f.write(f"{self}")

    def __repr__(self):
        return f'Size:{self.map.shape}\n{self.map}'

def solve_part2_v2(lines, filename):

    Path(os.path.join(os.path.dirname(__file__), "debug/v2/infinite_loops")).mkdir(parents=True, exist_ok=True)

    solved_map = Map_v2(lines)

    (is_done, is_in_infinite_loop) = (False, False)
    while not is_done and not is_in_infinite_loop:
        (is_done, is_in_infinite_loop) = solved_map.move_guard()

    solved_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/v2/solved_"+filename+".log"))
    # with open(filename, 'w') as f:
    #     for line in solved_map.map:
    #         f.write(f"{''.join(line)}\n")

    cells_to_try = solved_map.get_visited_cells_wo_start()

    infinite_loop_cnt = 0
    infinite_loop_positions = []

    start_time = time.time()

    for (i, j) in cells_to_try:
        current_iter_start_time = time.time()
        temp_map = Map_v2(lines)
        temp_map.map[i, j].set_to_barrier()
        
        (is_done, is_in_infinite_loop) = (False, False)

        while not is_done:
            (is_done, is_in_infinite_loop) = temp_map.move_guard()
            
            if is_in_infinite_loop:
                infinite_loop_positions.append((i, j))
                infinite_loop_cnt += 1
                temp_map.save_to_file(os.path.join(os.path.dirname(__file__), "debug/v2/"+filename+f'_(i,j):({i},{j})_{i*j}.log'))
                with open(os.path.join(os.path.dirname(__file__), "debug/v2/infinite_loops/"+filename+f'_infinite_loop_indexes.log'), 'a') as f:
                    f.write(f"{i},{j}\n")
                break

        iter_time = time.time() - current_iter_start_time
        total_time = time.time() - start_time
        print(f'(i,j):({i},{j}) \tinfinite_loop:{is_in_infinite_loop} \tinfinite_loop_cnt:{infinite_loop_cnt} \titer_time:{iter_time:.1f} \ttotal_time:{total_time:.1f}')

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


    p21 = solve_part2_v2(SIMPLE_INPUT_1, "part2_simple1")
    print(f'Part 2 (simple_1): {p21} Correct: {p21==0}')
    p22 = solve_part2_v2(SIMPLE_INPUT_2, "part2_simple2")
    print(f'Part 2 (simple_2): {p22} Correct: {p22==0}')


    p2 = solve_part2_v2(EXAMPLE_INPUT, "part2_example")
    print(f'Part 2 (example): {p2} Correct: {p2==6}')

    input_file = "solutions/day6/input.txt"
    lines = parse_file(input_file)
    map = Map(lines)

    p1 = solve_part1(map)
    print(f'\nPart 1: {p1} Correct:{p1==4967}')
    p2 = solve_part2_v2(lines, "part2_real")
    print(f'\nPart 2: {p2} Correct:{p2==1789}')

if __name__ == "__main__":
    main()

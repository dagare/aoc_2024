
import numpy as np

SIMPLE_INPUT = [
    '0123',
    '1234',
    '8765',
    '9876',
]

EXAMPLE_INPUT_1 = [
    '10..9..',
    '2...8..',
    '3...7..',
    '4567654',
    '...8..3',
    '...9..2',
    '.....01',
]

EXAMPLE_INPUT = [
    '89010123',
    '78121874',
    '87430965',
    '96549874',
    '45678903',
    '32019012',
    '01329801',
    '10456732',
]

def parse_file(file_path):

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    
    return lines

class Map:
    def __init__(self, lines):
        self.trail_heads = []

        self.map = np.empty((len(lines), len(lines[0])), dtype=object) 
        for (i, line) in enumerate(lines):
            for (j, height) in enumerate(list(line)):
   
                if height != '.':
                    self.map[i, j] = int(height)
                    if int(height) == 0:
                        self.trail_heads.append((i, j)) 
                else: 
                    self.map[i, j] = -1

        self.rows, self.cols = self.map.shape
                    
        
    def solve_trail_heads(self, find_distinct=False):

        sum = 0

        for trail_head in self.trail_heads:
            hilltops = self.solve_position(trail_head)
            
            if not find_distinct:
                hilltops = list(set(hilltops))
            
            sum += len(hilltops)

        return sum
    
    def solve_position(self, position):
        current_height_value = self.map[position[0],position[1]]

        next_positions = []
        next_positions.append((position[0]-1, position[1]))
        next_positions.append((position[0], position[1]+1))
        next_positions.append((position[0]+1, position[1]))
        next_positions.append((position[0], position[1]-1))

        results = []

        for (i, next_position) in enumerate(next_positions):
            if self.is_outside_bounds(next_position):
                continue
            
            if (current_height_value+1) != self.map[next_position[0], next_position[1]]:
                continue
            
            if self.map[next_position[0], next_position[1]] == 9:
                results.append((next_position[0], next_position[1]))
            else:
                results.extend(self.solve_position(next_position))
            
        return results

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
    
    def is_outside_bounds(self, position):
        (i, j) = position

        if i < 0:
            return True
        elif i > self.rows-1:
            return True
        elif j < 0:
            return True
        elif j >  self.cols-1:
            return True
        
        return False
    

    def __repr__(self):
        return f'Size:{self.map.shape}\n{self.map}'
    
def solve_part1(lines, debug=False):
    map = Map(lines)

    return map.solve_trail_heads()

def solve_part2(lines, debug=False):
    map = Map(lines)

    return map.solve_trail_heads(find_distinct=True)

def main():
    p1 = solve_part1(SIMPLE_INPUT, True)
    print(f'Part 1 (simple example): {p1} Correct: {p1==1}')

    p1 = solve_part1(EXAMPLE_INPUT_1, True)
    print(f'Part 1 (example_1): {p1} Correct: {p1==3}')

    p1 = solve_part1(EXAMPLE_INPUT, True)
    print(f'Part 1 (example): {p1} Correct: {p1==36}')

    input_file = "solutions/day10/input.txt"
    lines = parse_file(input_file)

    p1 = solve_part1(lines)
    print(f'\nPart 1: {p1}. Correct: {p1==733}')

    p2 = solve_part2(lines)
    print(f'\nPart 2: {p2}. Correct: {p2==1514}')

if __name__ == "__main__":
    main()
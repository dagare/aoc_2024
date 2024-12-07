EXAMPLE_INPUT = [
"190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20"
]

def parse_file(file_path):

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    
    return lines

class Calibration:
    def __init__(self, line):

        values = line.strip().split(':')
        self.target_sum = int(values[0])

        values = values[1].strip().split(' ')
        self.values = []
        for value in values:
            self.values.append(int(value))

    def is_solvable(self, operators):
            
        solvable = None
        for operator in operators:
            solvable = self.add_or_mul_recursivly(operator, operators, self.values[0], self.values[1:], [])
            if solvable:
                break

        return solvable  
    
    def add_or_mul_recursivly(self, operator, operators, left_value, numbers, current_sequence):
        current_sequence.append(operator)

        if operator == '+':
            left_value += numbers[0]
        elif operator == '*':
            left_value = left_value * numbers[0]
        elif operator == '|':
            left_value = int(str(left_value) + str(numbers[0]))

        # Early return for invalid path
        if left_value > self.target_sum:
            return None

        # We're at the end
        if len(numbers) == 1:
            if self.target_sum == left_value:
                return current_sequence
            
            return None

        # Else: continue down the tree
        sequence = None
        for operator in operators:
            sequence = self.add_or_mul_recursivly(operator, operators, left_value, numbers[1:], current_sequence)
            if sequence:
                break

        return sequence

def parse_lines(lines):
    
    calibrations = []

    for line in lines:
        calibrations.append(Calibration(line))
    
    return calibrations

def solve_part1(calibrations, print_debug=False):

    sum = 0

    for calibration in calibrations:
        solution_sequence = calibration.is_solvable(['+', '*'])
        if solution_sequence:
            if print_debug: print(f'CORRECT. {calibration.target_sum}: {calibration.values}, {solution_sequence}')
            sum += calibration.target_sum

    return sum

def solve_part2(calibrations, print_debug=False):

    sum = 0

    for calibration in calibrations:
        solution_sequence = calibration.is_solvable(['+', '*','|'])
        if solution_sequence:
            if print_debug: print(f'CORRECT. {calibration.target_sum}: {calibration.values}, {solution_sequence}')
            sum += calibration.target_sum

    return sum

def main():
   

    calibrations = parse_lines(EXAMPLE_INPUT)
    p1 = solve_part1(calibrations, True)
    print(f'Part 1 (example): {p1} Correct: {p1==3749}')
    p2 = solve_part2(calibrations, True)
    print(f'Part 2 (example): {p2} Correct: {p2==11387}')

    input_file = "solutions/day7/input.txt"
    lines = parse_file(input_file)
    calibrations = parse_lines(lines)

    print("\nPart 1:", solve_part1(calibrations))
    print("\nPart 2:", solve_part2(calibrations))

if __name__ == "__main__":
    main()
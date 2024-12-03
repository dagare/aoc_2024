import re

def parse_file_part1(file_path):
    matches = []

    with open(file_path, "r") as file:
        
        data = []

        for line in file:

            # Regular expression to find `mul(x,y)`
            pattern = r'mul\(([0-9]+),([0-9]+)\)'
            line_matches = re.findall(pattern, line)

            matches += line_matches
    
    return matches


def solve_part1(matches):
    sum = 0

    for match in matches:
        (x, y) = match
        sum += int(x) * int(y)

    return sum


def multiply_match(match):
    (x, y) = match
    return int(x) * int(y)


def parse_file(file_path):
    lines = ""

    with open(file_path, "r") as file:
        for line in file:
            lines += line
    
    return lines

def solve_part2(lines):
    sum = 0

    # Regular expression to find `mul(x,y)`
    pattern = r'mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don\'t\(\))'

    do = None

    line_matches = re.findall(pattern, lines)

    for line_match in line_matches:
        (x, y, _do, _dont) = line_match

        if bool(_do):
            do = True
        elif bool(_dont):
            do = False
        else:
            if do is None or do:
                sum += int(x) * int(y)

    return sum


def main():
    input_file = "solutions/day3/input.txt"
    part1_matches = parse_file_part1(input_file)

    print("\nPart 1:", solve_part1(part1_matches))

    part2_lines = parse_file(input_file)
    print("\nPart 2:", solve_part2(part2_lines))

if __name__ == "__main__":
    main()
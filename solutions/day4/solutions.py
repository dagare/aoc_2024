
def parse_file(file_path):
    lines = ""

    with open(file_path, "r") as file:
        for line in file:
            lines += line
    
    return lines

def solve_part1(lines):
    sum = 0
    return sum

def solve_part2(lines):
    sum = 0
    return sum

def main():
    input_file = "solutions/day4/input.txt"
    lines = parse_file(input_file)

    print("\nPart 1:", solve_part1(lines))
    print("\nPart 2:", solve_part2(lines))

if __name__ == "__main__":
    main()
from utils import read_input
import part1
import part2

def main():
    input_file = "solutions/day1/input.txt"
    data = read_input(input_file)

    print("Part 1:", part1.solve(data))
    print("Part 2:", part2.solve(data))

if __name__ == "__main__":
    main()
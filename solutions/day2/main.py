from utils import read_input
import part1
import part2

def main():
    input_file = "solutions/day2/input.txt"
    data = read_input(input_file)

    print("\nPart 1:", part1.solve(data))
    print("\nPart 2:", part2.solve(data))

if __name__ == "__main__":
    main()
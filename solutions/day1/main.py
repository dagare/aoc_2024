from utils import read_input
import part1
import part2

def main():
    simple_input_file = "solutions/day1/simple_input.txt"
    simple_data = read_input(simple_input_file)

    input_file = "solutions/day1/input.txt"
    data = read_input(input_file)

    print("\nPart 1:")
    print("Simple:", part1.solve(simple_data))
    print("Real  :", part1.solve(data))
    print("\nPart 2:")
    print("Simple:", part2.solve(simple_data))
    print("Real  :", part2.solve(data))

if __name__ == "__main__":
    main()
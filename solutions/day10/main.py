from pt1 import solve_part1 as solve_part1

def main():
    map = Map(SIMPLE_INPUT)
    # print(f'Before:\n{map}')
    p1 = solve_part1(map, True)
    # print(f'After:\n{map}')
    print(f'Part 1 (simple example): {p1} Correct: {p1==8}')

    map = Map(EXAMPLE_INPUT)
    # print(f'Before:\n{map}')
    p1 = solve_part1(map, True)
    # print(f'After:\n{map}')
    print(f'Part 1 (example): {p1} Correct: {p1==14}')

    map = Map(EXAMPLE_INPUT_P2)
    print(f'Before:\n{map}')
    p2 = solve_part2(map, True)
    print(f'After:\n{map}')
    print(f'Part 2 (example): {p2} Correct: {p2==9}')

    input_file = "solutions/day8/input.txt"
    lines = parse_file(input_file)
    map = Map(lines) 

    p1 = solve_part1(map)
    print(f'\nPart 1: {p1}. Correct: {p1==390}')

    p2 = solve_part2(map)
    print(f'\nPart 2: {p2}. Correct: {p2==1246}')

if __name__ == "__main__":
    main()
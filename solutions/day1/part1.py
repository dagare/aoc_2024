
def solve(data) -> int:
    """
    Solves Part 1 of the puzzle.
    :param data: Puzzle input data.
    :return: The solution to Part 1.
    """

    data[0].sort()
    data[1].sort()

    distance_sum = 0

    for number1, number2 in zip(data[0], data[1]):
        distance = abs(number1 - number2)
        distance_sum += distance

    return distance_sum
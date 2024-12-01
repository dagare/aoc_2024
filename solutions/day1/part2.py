
def solve(data) -> int:
    """
    Solves Part 2 of the puzzle.
    :param data: Puzzle input data.
    :return: The solution to Part 2.
    """
    
    similatity_score = 0

    for number_i in data[0]:
        occurrences = 0
        for number_j in data[1]:
            if number_i == number_j:
                occurrences += 1

        #print(f'number:{number_i}, occurrences:{occurrences}')

        similatity_score += number_i * occurrences

    return similatity_score
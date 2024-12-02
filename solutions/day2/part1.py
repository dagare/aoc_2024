
def solve(reports) -> int:
    """
    Solves Part 1 of the puzzle.
    :param data: Puzzle input data.
    :return: The solution to Part 1.
    """

    no_of_safe = 0

    for report in reports:
        prev_level = None
        is_increasing = None
        safe = True


        for level in report:
            # All increasing OR decreasing
            level = level

            # Is NOT first iteration
            if prev_level is not None:
                increasing = level > prev_level

                # We have taken inc/dec into consideration
                if is_increasing is None:
                    is_increasing = increasing

                elif is_increasing != increasing:
                    safe = False
                    print(f'Unsafe. is_increasing:{is_increasing}, increasing:{increasing}, \t report:{report}')
                    break


                diff = abs(level - prev_level)

                if diff < 1 or diff > 3:
                    safe = False
                    print(f'Unsafe. level:{level}, prev_level:{prev_level}, diff:{diff}\t report:{report}')
                    break

            prev_level = level

        if safe:
            no_of_safe += 1

    return no_of_safe
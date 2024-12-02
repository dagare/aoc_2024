
def is_report_safe(report):
    prev_level = None
    is_increasing = None

    for (i, level) in enumerate(report):
        # Is NOT first iteration
        if prev_level is not None:
            increasing = level > prev_level

            # We have taken inc/dec into consideration
            if is_increasing is None:
                is_increasing = increasing

            elif is_increasing != increasing:
                #print(f'Unsafe. report:{report}\tis_increasing:{is_increasing}, increasing:{increasing}')
                return (False, i, diff)


            diff = abs(level - prev_level)

            if diff < 1 or diff > 3:
                #print(f'Unsafe. report:{report}\tlevel:{level}, prev_level:{prev_level}, diff:{diff}')
                return (False, i, diff)

        prev_level = level

    return True, -1, diff

def solve(reports) -> int:
    """
    Solves Part 2 of the puzzle.
    :param data: Puzzle input data.
    :return: The solution to Part 2.
    """
    
    no_of_safe = 0

    for (report_index, original_report) in enumerate(reports):
        is_safe = False

        (test_is_safe, index, diff) = is_report_safe(original_report)

        if test_is_safe:
            is_safe = True
        else:
            for (level_index, level_value) in enumerate(original_report):
                report = original_report.copy()
                report.pop(level_index)
                (test_is_safe, index, diff) = is_report_safe(report)
                if test_is_safe:
                    is_safe = True
                    break

        # if not is_safe:
        #     report = original_report.copy()
        #     report.pop(index)
        #     print(f'Removing index:{index} \t{original_report}\t->{report}')
        #     (is_safe, index, diff) = is_report_safe(report)

        # # Then try move the level in front
        # if not is_safe:
        #     report = original_report.copy()
        #     report.pop(index-1)
        #     print(f'Removing index:{index-1} \t{original_report}\t->{report}')
        #     (is_safe, index, diff) = is_report_safe(report)


        if is_safe:
            no_of_safe += 1
        #else: 
        #    print(f'Unsafe report_index:{report_index }\tindex:{index}\treport:{original_report}, diff:{diff}')

    return no_of_safe
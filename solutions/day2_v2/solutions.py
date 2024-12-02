
def parse_input(file_path):

    with open(file_path, "r") as file:
        
        data = []

        for line in file:

            parts = line.split()

            data.append(list(map(int, parts)))

        return data

def solve_part1(reports):

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
                    #print(f'Unsafe. is_increasing:{is_increasing}, increasing:{increasing}, \t report:{report}')
                    break


                diff = abs(level - prev_level)

                if diff < 1 or diff > 3:
                    safe = False
                    #print(f'Unsafe. level:{level}, prev_level:{prev_level}, diff:{diff}\t report:{report}')
                    break

            prev_level = level

        if safe:
            no_of_safe += 1

    return no_of_safe

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

def solve_part2_v2(reports):

    no_of_safe = 0
    unsafe_indexes = []
    unsafe_reports = []

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

        if is_safe:
            no_of_safe += 1
            print(f'original_report:{original_report}->report:{report} makes it safe')
        else: 
        #    print(f'Unsafe report_index:{report_index }\tindex:{index}\treport:{original_report}, diff:{diff}')
            unsafe_indexes.append(report_index)
            unsafe_reports.append(original_report)

    return (no_of_safe, unsafe_indexes, unsafe_reports)

def solve_part2_v1(reports):

    no_of_safe = 0
    unsafe_indexes = []
    unsafe_reports = []

    for (report_index, original_report) in enumerate(reports):
        is_safe = False

        (test_is_safe, index, diff) = is_report_safe(original_report)

        if not is_safe:
            report = original_report.copy()
            report.pop(index)
            #print(f'Removing index:{index} \t{original_report}\t->{report}')
            (is_safe, index, diff) = is_report_safe(report)

        # Then try move the level in front
        if not is_safe:
            report = original_report.copy()
            report.pop(index-1)
            #print(f'Removing index:{index-1} \t{original_report}\t->{report}')
            (is_safe, unused, unused) = is_report_safe(report)

        # Corner case (move the item in front)
        if not is_safe and index > 1:
            report = original_report.copy()
            report.pop(index-2)
            #print(f'Removing index:{index-1} \t{original_report}\t->{report}')
            (is_safe, unused, unused) = is_report_safe(report)

        if is_safe:
            no_of_safe += 1
        else: 
        #    print(f'Unsafe report_index:{report_index }\tindex:{index}\treport:{original_report}, diff:{diff}')
            unsafe_indexes.append(report_index)
            unsafe_reports.append(original_report)

    return (no_of_safe, unsafe_indexes, unsafe_reports)

def main():
    input_file = "solutions/day2/input.txt"
    reports = parse_input(input_file)

    print("\nPart 1:", solve_part1(reports))

    (no_of_safe_v1, unsafe_indexes_v1, unsafe_reports_v1) = solve_part2_v1(reports)
    (no_of_safe_v2, unsafe_indexes_v2, unsafe_reports_v2) = solve_part2_v2(reports)
    print("\nPart 2 (v1):", no_of_safe_v1)
    print("\nPart 2 (v2):", no_of_safe_v2)

    diff_indexes = list(set(unsafe_indexes_v1) - set(unsafe_indexes_v2))

    print(f'Diff:{diff_indexes}')
    for diff_index in diff_indexes:
        print(f'index:{diff_index}\t report:{reports[diff_index]}')

if __name__ == "__main__":
    main()
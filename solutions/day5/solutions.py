import re

EXAMPLE_INPUT = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "     ",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47"
]

def parse_file(file_path):

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    
    return lines

class Rules:
    def __init__(self):
        self.data = {}

    def add(self, first, second):
        if first not in self.data:
            self.data[first] = []
        self.data[first].append(second)      

    def get(self, index):
        return self.data.get(index, [])
    
    def is_valid(self, first, second):
        if first not in self.data:
            return True
        
        if second not in self.get(first):
            return False
        
        return True
    
class Update:
    def __init__(self, pages):
        self.pages = [int(s) for s in pages]

        self.original_pages = self.pages

    def is_valid(self, rules):
        
        # Skip first requires adding one to index
        for (page_index, page) in enumerate(self.pages[1:]):
            page_index += 1
            first_half = self.pages[:page_index]
            # second_half = self.pages[page_index+1:]

            pages_that_cannot_come_before = rules.get(page)

            pages_that_cannot_come_before_set = set(pages_that_cannot_come_before)
            
            if any(item in first_half for item in pages_that_cannot_come_before_set):
                return False
            # common_items = [item for item in first_half if item in pages_that_cannot_come_before_set]
            # if common_items

        return True
    
    def try_to_fix(self, rules):

     
        for page_index in range(len(self.pages)):
            page = self.pages[page_index]
            # page_index += 1
            first_half_pages = self.pages[:page_index]

            pages_that_cannot_come_before = rules.get(page)
            pages_that_cannot_come_before_set = set(pages_that_cannot_come_before)
            
            for (idx, first_half_page) in enumerate(first_half_pages):
                if first_half_page in pages_that_cannot_come_before_set:
                    # time to swap
                    temp = self.pages[idx]
                    self.pages[idx] = self.pages[page_index]
                    self.pages[page_index] = temp

        
        return self.is_valid(rules)
    
    def middle(self):
        if len(self.pages) % 2 == 0:
            print(f'This is a even update!!!! {self.pages}')

        middle = len(self.pages) // 2

        return self.pages[middle]

def parse_lines(lines):
    
    # Find ordering rules
    rules = Rules()

    for line in lines:
        if '|' in line:
            values = line.strip().split('|')
            first = int(values[0])
            second = int(values[1])
            rules.add(first, second)

    # Find updates
    updates = []
    for line in lines:
        if ',' in line:
            updates.append(Update(line.strip().split(',')))
        
    return (rules, updates)

def solve_part1(rules, updates):
    sum = 0

    for update in updates:
        if update.is_valid(rules):
            middle_value = update.middle()
            sum += middle_value

    return sum

def solve_part2(rules, updates):
    

    invalid_updates = []
    for update in updates:
        if not update.is_valid(rules):

            invalid_updates.append(update)


    sum = 0

    for invalid_update in invalid_updates:
        # while not invalid_update.is_valid(rules):
        #     is_valid = invalid_update.try_to_fix(rules)
        #     print(f'Retrying to fix. Valid:{is_valid} {invalid_update.original_pages} -> {invalid_update.pages}')
        invalid_update.try_to_fix(rules)

        middle_value = invalid_update.middle()
        sum += middle_value

    return sum


def main():
   

    (example_rules, example_updates) = parse_lines(EXAMPLE_INPUT)
    p1 = solve_part1(example_rules, example_updates)
    print(f'Part 1 (example): {p1} Correct: {p1==143}')
    p2 = solve_part2(example_rules, example_updates)
    print(f'Part 2 (example): {p2} Correct: {p2==123}')

    input_file = "solutions/day5/input.txt"
    lines = parse_file(input_file)
    (rules, updates) = parse_lines(lines)

    print("\nPart 1:", solve_part1(rules, updates))
    print("\nPart 2:", solve_part2(rules, updates))

if __name__ == "__main__":
    main()
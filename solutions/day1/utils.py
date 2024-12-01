
def read_input(file_path: str) -> str:
    """
    Reads the puzzle input from a file.
    :param file_path: Path to the input file.
    :return: Raw input as a string.
    """
    with open(file_path, "r") as file:
        
        column1 = []
        column2 = []

        for line in file:

            parts = line.split()

            number1, number2 = map(int, parts)

            column1.append(number1)
            column2.append(number2)

        return [column1, column2]
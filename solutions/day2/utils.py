
def read_input(file_path: str) -> str:
    """
    Reads the puzzle input from a file.
    :param file_path: Path to the input file.
    :return: Raw input as a string.
    """
    with open(file_path, "r") as file:
        
        data = []

        for line in file:

            parts = line.split()

            m = map(int, parts)
            l = list(map(int, parts))

            data.append(list(map(int, parts)))

        return data
    

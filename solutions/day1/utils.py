
def read_input(file_path: str) -> str:
    """
    Reads the puzzle input from a file.
    :param file_path: Path to the input file.
    :return: Raw input as a string.
    """
    with open(file_path, "r") as file:
        return file.read().strip()
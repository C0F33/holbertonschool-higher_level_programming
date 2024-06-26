#!/usr/bin/python3
def print_square(size):
    """This function prints a square with the character #.

    Args:
        size (int): The size of the square.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

if __name__ == '__main__':
	print_square()
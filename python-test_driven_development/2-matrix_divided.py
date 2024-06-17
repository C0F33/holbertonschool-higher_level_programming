#!/usr/bin/python3
def matrix_divided(matrix, div):
	"""
	Divides all elements of a matrix by a given divisor.

	Args:
		matrix (list): A matrix represented as a list of lists.
		div (int or float): The divisor.

	Returns:
		list: A new matrix with the elements divided by the divisor.

	Raises:
		TypeError: If the matrix is not a matrix of integers/floats or if the divisor is not a number.
		ZeroDivisionError: If the divisor is zero.

	Example:
		matrix = [[1, 2, 3], [4, 5, 6]]
		div = 2
		matrix_divided(matrix, div)  # Output: [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
	"""


	if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	if len(set(len(row) for row in matrix)) > 1:
		raise TypeError("Each row of the matrix must have the same size")

	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")

	new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

	return new_matrix


if __name__ == "__main__":
    matrix_divided()

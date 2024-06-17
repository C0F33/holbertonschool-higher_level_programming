#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
	"""This function prints a name.

	Args:
		first_name (str): The first name.
		last_name (str): The last name. Defaults to an empty string.

	Returns:
		None
	"""
	if type(first_name) is not str:
		raise TypeError("first_name must be a string")
	if type(last_name) is not str:
		raise TypeError("last_name must be a string")
	print("My name is {} {}".format(first_name, last_name))

if __name__ == '__main__':
	say_my_name()
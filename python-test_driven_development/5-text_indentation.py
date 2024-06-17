#!/usr/bin/python3
def text_indentation(text):
    """This function prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    print(result.strip())
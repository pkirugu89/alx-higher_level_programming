#!/usr/bin/python3
""" Method that indents text."""


def text_indentation(text):
    """
    Method that indent text and split it
    Args:
        text (str): text to be indented.
    Returns:
        str: returns a formatted string.
    """
    # check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Split the text based on ".", "?", and ":"
    split_text = text.split(".")
    temp_text = []
    for item in split_text:
        temp_text.extend(item.split("?"))
    final_text = []
    for item in temp_text:
        final_text.extend(item.split(":"))

    # Remove empty strings and strip leading/trailing whitespace
    split_text = [line.strip() for line in final_text if line.strip() != ""]

    # Print the formatted text
    formatted_text = "\n\n".join(split_text)
    print(formatted_text)

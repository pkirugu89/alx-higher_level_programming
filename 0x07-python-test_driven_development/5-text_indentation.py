#!/usr/bin/python3
""" Text indentation method. """


def text_indentation(text):
    """
    Method that indent text and split it
    Args:
        text (str): text to be indented
    Returns:
    str: returns a formatted string.
    """
    # check if the text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # split the text based on ".", "?" and ":"
    split_text = text.split(".") + text.split("?") + text.split(":")
    # Remove empty strings and strip leading/trailing whitespace
    split_text = [line.strip() for line in split_text if line.strip() != ""]

    # print formatted text
    formatted_text = "\n\n".join(split_text)
    print(formatted_text)

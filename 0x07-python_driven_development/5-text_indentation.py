#!/usr/bin/python3

def text_indentation(text):
    # check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Split the text based on ".", "?", and ":"
    split_text = text.split(".") + text.split("?") + text.split(":")
    # Remove empty strings and strip leading/trailing whitespace
    split_text = [line.strip() for line in split_text if line.strip() != ""]
    # Print the formatted text
    formatted_text = "\n\n".join(split_text)
    print(formatted_text)

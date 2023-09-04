#!/usr/bin/python3
""" Method that print first name and last name """


def say_my_name(first_name, last_name=""):
    """
    Method that prints the firstname and lastname.
    Args:
        first_name (str): first parameter of the method.
        last_name (str): second parameter of the method.

    Returns:
    str: returns the full name of the user.

    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # chack if the last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # print the names
    print(f"My name is {first_name} {last_name}")

#!/usr/bin/python3
""" Say my name method. """


def say_my_name(first_name, last_name=""):
    # check if the first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # check if the last_name is a string
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # print both first_name and last_name
    else:
        print(f"My name is {first_name} {last_name}")

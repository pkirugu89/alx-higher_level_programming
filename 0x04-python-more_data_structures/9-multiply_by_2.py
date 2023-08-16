#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multi_dict = {}
    # Iterate through the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 & store the value in new dict
        multi_dict[key] = value * 2
    return multi_dict

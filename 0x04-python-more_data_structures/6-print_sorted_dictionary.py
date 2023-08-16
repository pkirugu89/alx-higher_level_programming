#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys in alphabetic order
    sort_keys = sorted(a_dictionary.keys())
    # Iterate through the sorted keys and print the key-value pairs
    for k in sort_keys:
        value = a_dictionary[k]
        print("{}: {}".format(k, value))

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return list_copy  # Return a copy of the original list
    else:
        # Create a new list with the element replaced
        new_list = list_copy
        new_list[idx] = element
        return new_list

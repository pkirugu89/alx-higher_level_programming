#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_int = set()
    # Iterate through the elements in the input list
    for x in my_list:
        # Add the x to the set(sets automatically handle duplicates)
        unique_int.add(x)
    # Calculate the sum of the unique integers
    sum_uniq = sum(unique_int)
    return sum_uniq

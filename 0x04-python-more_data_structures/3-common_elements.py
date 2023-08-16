#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create a new set to store the common elements
    com_set = set()
    # Iterate through the elements in the first set
    for x in set_1:
        # If x is also in the 2nd set,add it to the common set
        if x in set_2:
            com_set.add(x)
    return com_set

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # create new sets to store unique elements from each set
    u_set_1 = set()
    u_set_2 = set()
    # Iterate through the elements in the first set
    for x in set_1:
        # If the x is not in the 2nd set,add it to unique_elements_set_1
        if x not in set_2:
            u_set_1.add(x)
    # Iterate through the elements in the second set
    for x in set_2:
        # If the x is not in the 1st set,add it to unique_elements_set_2
        if x not in set_1:
            u_set_2.add(x)
    # Combine the two sets of unique elements to get the result
    diff_element_set = u_set_1.union(u_set_2)
    return diff_element_set

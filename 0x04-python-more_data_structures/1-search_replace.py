#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced values
    r_list = []
    # Iterate through the elements in the original list
    for x in my_list:
        # If the element matches the search value,replace it with the new value
        if x == search:
            r_list.append(replace)
        else:
            r_list.append(x)
    return r_list

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # define the list length of my_list
    list_len = len(my_list)
    if idx < 0 or idx > list_len - 1:
        # Return the same list if idx is -ve or out of range
        return my_list
    else:
        new_list = my_list
        del new_list[idx]
        return new_list

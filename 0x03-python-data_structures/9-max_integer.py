#!/usr/bin/python3
def max_integer(my_list=[]):
    # define length of my_list
    list_len = len(my_list)
    # Return None if the list is empty
    if list_len == 0:
        return None
    else:
        # Initialize the maximum value with the first element of the list
        max_val = my_list[0]
        # Iterate through the list to find the maximum value
        for num in range(list_len):
            if my_list[num] > max_val:
                max_val = my_list[num]

        return max_val

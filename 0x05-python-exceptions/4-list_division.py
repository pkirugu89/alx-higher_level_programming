#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # initialize an empty list for storing division results
    result_list = []
    try:
        for i in range(list_length):
            # Access elementd from 2 lists
            list_1 = my_list_1[i] if i < len(my_list_1) else 0
            list_2 = my_list_2[i] if i < len(my_list_2) else 0

            # check if the elements are int or floats
            if not isinstance(list_1, (int, float)) or not isinstance(list_2, (int, float)):
                print("wrong type")
                result_list.append(0)
            elif list_2 == 0:
                # checks division by 0
                print("division by 0")
                result_list.append(0)
            else:
                # Perform the division and append the result to the result list
                result_list.append(list_1 / list_2)
    except IndexError:
        print("out of range")
        result_list.append(0)
    finally:
        return result_list

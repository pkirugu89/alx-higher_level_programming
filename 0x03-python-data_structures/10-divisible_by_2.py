#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    result = []
    for num in range(list_len):
        if my_list[num] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

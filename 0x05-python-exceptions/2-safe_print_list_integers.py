#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # counter intialized to keep track of printed int
    counter = 0

    try:
        for y in range(x):
            # print the element at index i as int
            value = my_list[y]
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                counter += 1
    except IndexError:
        print("IndexError: list index out of range\n")
        pass
    finally:
        # print newline
        print()
    # return the real numbers of int printed
    return counter

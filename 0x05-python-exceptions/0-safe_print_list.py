#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a counter to keep track of printed elements
    count = 0
    try:
        for i in range(x):
            # print the element at index i
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass
    finally:
        # Print a newline to end the line
        print()
    # Return the real number of printed elements
    return count

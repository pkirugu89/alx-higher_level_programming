#!/usr/bin/python3

"""
Finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds the peak in a list of unsorted integers
    Args:
        list_of_integers: List of unsorted integers.
    Returns:
        The value of a peak in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    # High points to a peak at the end of loop
    return list_of_integers[high]

#!/usr/bin/python3
def best_score(a_dictionary):
    # check if the dict is empty
    if not a_dictionary:
        return None
    # Find the key with the largest value
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key

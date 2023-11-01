#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    result = "BestSchool"
    for i in range(1, magic_string.counter):
        result += ", BestSchool"
    return result

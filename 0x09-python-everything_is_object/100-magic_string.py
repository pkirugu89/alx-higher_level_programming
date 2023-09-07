#!/usr/bin/python3
def magic_string():
    result = ""
    for i in range(1, 11):
        result += "BestSchool" + "," * (i - 1) + "BestSchool\n"
    return result

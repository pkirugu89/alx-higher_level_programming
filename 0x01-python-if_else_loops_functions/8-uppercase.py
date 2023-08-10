#!/usr/bin/python3
def uppercase(s):
    result = ''
    for c in s:
        # Check if the character is lowercase and convert to uppercase
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    # Print a new line after processing the string
    print("{}".format(result))

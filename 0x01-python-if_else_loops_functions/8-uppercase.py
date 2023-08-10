#!/usr/bin/python3
def uppercase(s):
    for c in s:
        # Check if the character is lowercase and convert to uppercase
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - ord('a') + ord('A')), end='')
        else:
            print(c, end='')
    # Print a new line after processing the string
    print()

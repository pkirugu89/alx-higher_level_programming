#!/usr/bin/python3
def roman_to_int(roman_string):
    # check if the input isn't a string or is None
    if not isinstance(roman_string, str) or not roman_string:
        # Return 0 if not a valid roman numeral
        return 0
    # Dictionary to map the Roman numerals to their coresponding values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    # Initialize variables to keep track of previous abd total values
    prev_val = 0
    total_val = 0
    # Iterate through thr chars of Roman string in reverse order
    for char in roman_string[::-1]:
        value = roman_values[char]
        # Compare the current value with the previous value
        if value >= prev_val:
            total_val += value  # Add value to the total
        else:
            # Subtract the value if it's a substraction case
            total_val -= value
        # Update the previous value for the next iteration
        prev_val = value
    # Return the final integer value
    return total_val

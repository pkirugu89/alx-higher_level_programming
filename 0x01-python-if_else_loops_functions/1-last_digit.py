#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Extract the last digit of the number
last_digit = abs(number) % 10
# handles negative last digit if number id less than 0
if number < 0:
    last_digit = -last_digit
# Determine the description based on the last digit
if last_digit > 5:
    description = "greater than 5"
elif last_digit == 0:
    description = "0"
else:
    description = f"less than 6 and not 0"
# print the desired output
print(f"Last digit of {number} is {last_digit} and is {description}")

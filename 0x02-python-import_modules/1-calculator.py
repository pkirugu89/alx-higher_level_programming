#!/usr/bin/python3
if __name__ == "__main__":
    # import calculator-1
    from calculator_1 import add, sub, mul, div
    # declaration of var a and b
    a = 10
    b = 5

    # output the results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

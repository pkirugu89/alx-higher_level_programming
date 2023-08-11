#!/usr/bin/python3
if __name__ == "__main__":
    # import calculator-1
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    sum1 = add(a, b)
    sub1 = sub(a, b)
    mul1 = mul(a, b)
    div1 = div(a, b)
    # output the results
    print("{} + {} = {}".format(a, b, sum1))
    print("{} - {} = {}".format(a, b, sub1))
    print("{} * {} = {}".format(a, b, mul1))
    print("{} / {} = {}".format(a, b, div1))

#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    # import calculator-1
    from calculator_1 import add, sub, mul, div
    sum1 = add(a, b)
    sub1 = sub(a, b)
    mul1 = mul(a, b)
    div1 = div(a, b)
    # output the results
    print(f"{a} + {b} = {sum1}")
    print(f"{a} - {b} = {sub1}")
    print(f"{a} * {b} = {mul1}")
    print(f"{a} / {b} = {div1}")

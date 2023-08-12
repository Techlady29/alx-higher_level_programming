#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import sub, add, div, mul

    a = 10
    b = 5

    print("{:c} - {:c} = {:c}".format(a, b, sub(a, b)))
    print("{:c} + {:c} = {:c}".format(a, b, add(a, b)))
    print("{:c} / {:c} = {:c}".format(a, b, div(a, b)))
    print("{:c} * {:c} = {:c}".format(a, b, mul(a, b)))

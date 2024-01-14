# Given two numbers. The task is to find the GCD of the two numbers.

def gcd_1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a%b)
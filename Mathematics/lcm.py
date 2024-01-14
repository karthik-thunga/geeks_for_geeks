# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers. 


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a,b)

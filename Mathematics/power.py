# Given two integers x and n, write a function to compute xn. 
# We may assume that x and n are small and overflow doesn’t happen.


def power_rec(x, n):
    if n == 0: return 1
    temp = power_rec(x, n//2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

def power_bit_iterative(x, n):
    power = 1
    while n > 0:
        if n % 2 == 1:
            power *= x
        x *= x
        n = n // 2
    return power
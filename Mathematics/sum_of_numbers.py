# Given a number n, find the sum of first natural numbers.

def sum_of_nums(n):
    # To avaoid overflow
    if n % 2 == 0:
        return (n//2) (n+1)
    return n((n+1)//2)
# Given an integer n, 
# write a function that returns count of trailing zeroes in n!.  

def factorial(n):
    return 1 if (n == 0 or n==1) else n * factorial(n-1)

def trailing_zero(n):
    fact = factorial(n)
    num_digit = 0
    while fact % 10 == 0:
        num_digit += 1
        fact = fact // 10
    return num_digit

# Given an integer, write a function that returns true if the given number is palindrome, else false. 
# For example, 12321 is palindrome, but 1451 is not palindrome.

def is_palindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    return rev == n 

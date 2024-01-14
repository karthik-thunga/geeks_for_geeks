# Given a number n, write an efficient function to print all prime factors of n. 
# For example, if the input number is 12, then output should be “2 2 3”. 
# And if the input number is 315, then output should be “3 3 5 7”.

def is_prime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def prime_factor(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i ,end=" ")

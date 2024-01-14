# Given a positive integer, check if the number is prime or not. 
# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Examples of first few prime numbers are {2, 3, 5}.

def is_prime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
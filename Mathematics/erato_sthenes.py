# Sieve of Eratosthenes is a method for finding all primes up to (and possibly including) a given natural. 
# This method works well when is relatively small, 
# allowing us to determine whether any natural number less than or equal to is prime or composite. 

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    i = 2
    while i*i <= n:
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
        i += 1
    for i in range(2, n+1):
        if primes[i]:
            print(i, end=" ")

# Given a natural number n, print all distinct divisors of it.

def divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            if n != i*i:
                print(i, end=" ")
        i += 1
    
    while i > 0:
        if n % i == 0:
            print(n//i, end=" ")
        i -= 1

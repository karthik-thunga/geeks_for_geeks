# Find floor sqareroot of t number

def sqrt_(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return i - 1
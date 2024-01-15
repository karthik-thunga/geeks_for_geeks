# Given an array of size n, write a program to check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.

def is_sorted(li):
    sorted = True

    if len(li) <= 1:
        return sorted
    prev = li[0]
    for i in range(1, len(li)):
        if li[i] < prev:
            sorted = False
            break
    return sorted

# Given an array of size n, write a program to check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.

def is_sorted(arr, n):
    sorted = 1
    if n <= 1:
        return sorted
    asc = False
    if arr[0] < arr[n-1]:
        asc = True
    if asc:
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                sorted = 0
                break
    else:
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                sorted = 0
                break
    return sorted

print(is_sorted([1,2,3,5,1], 5))

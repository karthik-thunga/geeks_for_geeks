# Find occurence of a number in sorted array.

def first_occ(arr, x):
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = (l+h) // 2

        if arr[m] > x:
            h = m - 1
        elif arr[m] < x:
            l = m + 1
        elif m == 0 or arr[m-1] != arr[m]:
            return m
        else:
            h = m - 1
    return -1

def last_occ(arr, x):
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = (l+h) // 2

        if arr[m] > x:
            h = m - 1
        elif arr[m] < x:
            l = m + 1
        elif m == len(arr) - 1 or arr[m+1] != arr[m]:
            return m
        else:
            l = m + 1
    return -1

def find_occ(arr, x):
    first_occu = first_occ(arr, x)
    if first_occu == -1:
        return 0
    last_occu = last_occ(arr, x)
    return last_occu - first_occu + 1
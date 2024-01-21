# Count 1's in sorted binary list

def first_occ(arr, x):
    l = 0
    h = len(arr) -1

    while l <= h:
        m = (l+h) // 2
        if arr[m] > x:
            l = m + 1
        elif arr[m] < x:
            h = m - 1
        elif m == len(arr)-1 or arr[m+1] != arr[m]:
            return m
        else:
            l = m + 1
    return -1

def count_one(arr):
    first_occu = first_occ(arr, 1)
    print(f"last : {first_occu}")
    if first_occu == -1:
        return 0
    return len(arr)-1 - first_occu

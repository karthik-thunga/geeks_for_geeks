def find_last_occ(arr, x):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            h = m - 1
        elif m == (len(arr) - 1) or arr[m+1] != arr[m]:
            return m
        else:
            l = m + 1 
    return -1
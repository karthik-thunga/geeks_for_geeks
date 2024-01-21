# Find peak element

def peakElement(arr, n):
        # Code here
        for i in range(n):
            if i == 0:
                if  arr[i] > arr[i+1]:
                    return arr[i]
                continue
            elif i == n-1:
                if arr[i] > arr[i-1]:
                    return arr[i]
                continue
            elif arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return arr[i]
        return -1
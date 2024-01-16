# Reserve a list

def reserse_list(arr, n):
    if n <= 1:
        return arr
    start = 0
    end = n - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -=1
    return arr

def reserse_list(li):
    if len(li) <= 1:
        return li
    reversed_list = []
    for i in range(len(li)-1, -1, -1):
        reversed_list.append(li[i])
    return reversed_list



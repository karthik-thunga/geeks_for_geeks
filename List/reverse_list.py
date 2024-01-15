# Reserve a list

def reserse_list(li):
    if len(li) <= 1:
        return li
    reversed_list = [None] * len(li)
    start = 0
    end = len(li) - 1
    while start <= end:
        reversed_list[start] = li[end]
        reversed_list[end] = li[start]
        start += 1
        end -=1
    return reversed_list

def reserse_list(li):
    if len(li) <= 1:
        return li
    reversed_list = []
    for i in range(len(li)-1, -1, -1):
        reversed_list.append(li[i])
    return reversed_list



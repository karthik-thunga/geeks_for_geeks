# Left Rotate a list by one

def left_rotate1(li):
    if len(li) <= 1:
        return li
    li.append(li.pop(0))
    return li

def left_rotate2(li):
    if len(li) <= 1:
        return li
    first = li[0]
    for i in range(1, len(li)):
        li[i-1] = li[i]
    
    li[-1] = first
    return li

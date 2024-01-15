# Given a sorted array, the task is to remove the duplicate elements from the array.

def remove_dup1(li):
    # if list is [] or [1] return, list
    if len(li) <= 1:
        return li
    removed_dub = []
    removed_dub.append(li[0])
    for i in range(1,len(li)):
        # check element seen before(till i)
        if li[i] != li[i-1]:
            removed_dub.append(li[i])
    return removed_dub

def remove_dup2(li):
    # if list is [] or [1] return, list
    if len(li) <= 1:
        return li
    removed_dub = []
    lookup = set()
    for ele in li:
        # check element in lookup
        if ele not in lookup:
            removed_dub.append(ele)
            lookup.add(ele)
    return removed_dub


    

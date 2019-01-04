def sorted_copy(lst):
    copy = list(lst)
    copy.sort()
    return copy

def merge_lists(list1, list2):
    return list(set(list1).union(set(list2)))


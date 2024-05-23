# a function for a binary search algorithm
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    # determine the midpoint
    while first <= last:
        midpoint = (first + last)//2

    # evaluate whether value at midpoint is our target value
    if list[midpoint] == target:
        return midpoint
    elif list[midpoint] < target:
        first = midpoint + 1
    else:
        last = midpoint - 1

    return None

# Linear Search Algorithm
def linear_search(list, target):
    """
    Returns an index position of the target value if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i   
    return None





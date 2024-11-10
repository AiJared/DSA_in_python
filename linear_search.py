# Linear Search Algorithm
def linear_search(list, target):
    """
    Returns an index position of the target value if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i   
    return None


# A function to verify the linear search algorithm above
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

# list of values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# check if our algorithm works
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)

# A Class to demonstrate linear search
class LinearSearch:
    # constructor to initialize the list of values
    def __init__(self, lst):
        self.lst = lst
    
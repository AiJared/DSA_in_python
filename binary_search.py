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

# A function to verify the binary search algorithm above
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

# list of values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# check if our algorithm works
result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

# Binary Search Algorithm cal also be implemented using a class as show below
class BinarySearch:
    # Initialize the list of values
    def __init__(self, lst):
        self.lst = lst
    
    
    

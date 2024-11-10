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
    
    # method to actually do linear search
    def linear_search(self, target):
        """
        Search for the value in the list starting from the first index value.
        If the value is in the list return its index value. If not return None.
        """
        for i in range(0, len(self.lst)):
            if self.lst[i] == target:
                return i
        return None
    
    # Method to verify the results of the linear search method above
    def verify(self, index):
        """
        If index is available print it. If it is not available print the value is not found.
        """
        if index is not None:
            print("Target found at index: ", index)
        else:
            print("Target not found!")

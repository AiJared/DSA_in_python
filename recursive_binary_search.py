# This one will behave a bit differently than the first binary search function.
# Instead of returning an index value, it will return a True value if it exists and 
# False if it does not
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        # find the midpoint
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 12)
verify(result)            

result = recursive_binary_search(numbers, 6)
verify(result) 

# Recursive Binary Search can be implemented inside a class
class RecursiveBinarySearch:
    # Initialize the list of values
    def __init__(self, lst):
        self.lst = lst
    
    # Method that carries out the recursive binary search
    def recursive_binary_search(self, target):
        # Return False if the list is empty
        if len(self.lst) == 0:
            return False
        else:
            # Determine the midpoint then compare it to the midpoint and adjust from there 
            # depending on whether the target is less or greater than the midpoint value
            midpoint = len(self.lst) // 2
            if self.lst[midpoint] == target:
                return True
            else:
                # Recursively adjust the midpoint depending on the size of the midpoint
                # in comparison to the midpoint
                if self.lst[midpoint] < target:
                    return recursive_binary_search(self.lst[midpoint+1:], target)
                else:
                    return recursive_binary_search(self.lst[:midpoint], target)
    
    # Method to verify the results of the recursive_binary_search() method above
    def verify(self, result):
        print("Target found: ", result)

# Create a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Instantiate the RecursiveBinarySearch object
re_binary_search = RecursiveBinarySearch(nums)


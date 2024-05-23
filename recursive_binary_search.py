# This one will behave a bit differently that the first binary search function.
# Instead of returning an index value, it will return a True value if it exists and False if it does not
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
# List in python
new_list = [1, 2, 3]
# accessing a value in an array using index
result = new_list[0]
print(result)

# trying to access an index value larger than what already exists in the array 
# would result into the array crashing and give an IndexError.
# For Example
# print(new_list[5])

"""
To search for an item in a list we can use one of two methods
"""
# searching using an in operator
"""
checks if a list contains an item
"""
if 1 in new_list: print(True)

"""
The in operator actually calls a contains method that is defined in a list type
which runs in a linear search operation.

In addition to this we can use a for loop to iterate over the list manually and
perform a comparison operation.
"""

for n in new_list:
    if n == 1:
        print(True)

        break

"""
This is more or less the implementation of linear search
"""
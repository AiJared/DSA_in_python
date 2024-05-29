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

# Creating a new list, the list doesn't know the size of the list or how many items it will store
# Below is an empty list
numbers = [] # this is an empty list with a space of 1
"""
Since n in the list is 0, there are no elements in the array above
Space is allocated for one element the list to start off. Because the 
space allocated for the list and the space used by the list are not
the same, what do you think happens when we ask Python for the length
of the list?
"""
len(numbers)
"""
Well it will give us 0. This means that the list does not use memory allocation
as an indication of it's size.

Okay so this list numbers currently has space for one element, now let's use
append method to insert a number at the end of the list 
"""
numbers.append(2)

"""
Now the memory allocation and the size of the list are the same since the list
contains one element. Now when we try to add another element using the same append
method, first we should keep in mind that the list had only one space for one element
which was taken by 2, so here, it would have to allocate another space for our second
item and thereby the size of the list. It does this by calling list resize operation.

"""
numbers.extend([4, 5, 6])
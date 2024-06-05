import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quicksort(values):
    if len(values) <= 1:
        return values
    
sorted_numbers = quicksort(numbers)
print(sorted_numbers)


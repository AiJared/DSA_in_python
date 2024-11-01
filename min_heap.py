# Python's heapq module allows us to use lists as heaps efficiently.
import heapq

# Creating a Min Heap
heap = []
# Create a list of numbers
numbers = [20, 15, 10, 30, 40]
# Loop through the list of numbers as we push the elements to the heap list
for num in numbers:
    heapq.heappush(heap, num)

# output the heap inform of a list
print("Min-Heap: ", heap)
# Remove the smallest element from the heap then output it
print("Smallest Element: ", heapq.heappop(heap))
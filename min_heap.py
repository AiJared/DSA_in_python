# Python's heapq module allows us to use lists as heaps efficiently.
import heapq

# Creating a Min Heap
heap = []

numbers = [20, 15, 10, 30, 40]

for num in numbers:
    heapq.heappush(heap, num)

# output the heap inform of a list
print("Min-Heap: ", heap)

# Remove the smallest element from the heap then output it
print("Smallest Element: ", heapq.heappop(heap))
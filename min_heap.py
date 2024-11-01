# Python's heapq module allows us to use lists as heaps efficiently.
import heapq

heap = []

numbers = [20, 15, 10, 30, 40]

for num in numbers:
    heapq.heappush(heap, num)
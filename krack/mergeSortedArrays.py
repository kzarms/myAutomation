# https://medium.com/outco/how-to-merge-k-sorted-arrays-c35d87aa298e

# Space: O(NK) (Plus O(K) for the heap)
# Time: O(NK log(K))
"""
import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements

heapq.heapify(H)

print(H)

a = [3, 4, 7, 9]
b = [1, 2, 5, 12]
c = [6, 8, 10, 11]

minHeap = []
heapq.heapify(minHeap)

heapq.heappush(minHeap, 3)
heapq.heappop(minHeap)

print(minHeap)


def sortNsortedArrays(*arrays):
    # My min heap for sorting
    min_heap = []
    result_list = []

    for arr in arrays:
        for el in arr:
            heapq.heappush(min_heap, el)
    print(min_heap)

    while min_heap:
        result_list.append(heapq.heappop(min_heap))

    print(result_list)


sortNsortedArrays(a, b, c)

"""

import heapq
from timeit import default_timer as timer

def get_k_docs(*arrays):
    min_heap = []
    results = []
    for arr in arrays:
        for el in arr:
            heapq.heappush(min_heap, el)

    while min_heap:
        results.append(heapq.heappop(min_heap))
    print(results)


def bf_sort(*arrays):
    result = []
    for arr in arrays:
        for el in arr:
            result.append(el)
    result.sort()
    print(result)

a = [3, 4, 7, 9]
b = [1, 2, 5, 12]
c = [6, 8, 10, 11]

start = timer()
get_k_docs(a, b, c)
end = timer()
print(end - start)

start = timer()
bf_sort(a, b, c)
end = timer()
print(end - start)

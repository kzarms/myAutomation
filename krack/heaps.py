#!/usr/bin/python3
""" Heap examples """

# Binary heap
ARR = [10, 15, 30, 40, 50, 100, 40, 60, 70, 60, 80, 120, 140, 90, 110]

# min
print(ARR[0])

i = 2
print(ARR[int(i - 1 / 2)])    # Parrent
print(ARR[int((i + 1) + 1)])  # left child node
print(ARR[int((i + 1) + 2)])  # right child node



### k largest element in array ###

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3

from heapq import *

def kLelement(arr, k):
    maxHeap = []

    for el in arr:
        heappush(maxHeap, el)
        if len(maxHeap) > k:
            heappop(maxHeap)

    return maxHeap

print(kLelement(arr, k))

def kLelement2(arr, k):
    arr.sort()
    return arr[len(arr) - k:]

print(kLelement2(arr, k))
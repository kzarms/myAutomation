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


### n ROPES #####

from heapq import *

arr = [2, 3, 4, 6]

def minCost(arr):
    heapify(arr)
    totalCost = 0
    while len(arr) > 1:
        min1 = heappop(arr)
        min2 = heappop(arr)
        cost = min1 + min2
        heappush(arr, cost)
        totalCost += cost

    return totalCost

print(minCost(arr))

arr = [2, 3, 4, 6]
def minCost2(arr):

    totalCost = 0

    while len(arr) > 1:
        min1 = min(arr)
        arr.remove(min1)
        min2 = min(arr)
        arr.remove(min2)
        cost = min1 + min2
        totalCost += cost
        arr.append(cost)

    return totalCost

print(minCost2(arr))

###### Max distinct elements ##########

arr = [5, 7, 5, 5, 1, 2, 2]
k = 3

def maxDist(arr, k):
    h = {}
    for i in range(len(arr)):
        if arr[i] in h:
            h[arr[i]] += 1
        else:
            h[arr[i]] = 1

    count = 0
    minHeap = []
    for key in h.keys():
        if h[key] > 1:
            heappush(minHeap, h[key])
        else:
            count += 1

    while k > -1 and minHeap:
        val = heappop(minHeap)
        if val == 1:
            count += 1
        else:
            k -= 1
            val -= 1
            heappush(minHeap, val)

    return count


print(maxDist(arr, k))


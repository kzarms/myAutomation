# find kth largest number
stream = [1, 2, 3, 5, 6, 8, 56, 13, 14]

k = 5


def findL(stream, k):
    if k == 0:
        return None

    result = []
    for i in range(k):
        result.append(max(stream))
        stream.remove(result[i])
    return result[-1]


print(findL(stream, k))


from heapq import *


stream = [1, 2, 6, 7, 23, 33, 5, 54, 12]
k = 3


def kth(stream, k):
    minHeap = []

    for el in stream:
        heappush(minHeap, el)

        if len(minHeap) > k:
            heappop(minHeap)

    return minHeap[0]


print(kth(stream, k))


###########################################################
stream = [4, 1, 3, 12, 7, 14]
K = 3

from heapq import *


class KthLargestNumberInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.minHeap, num)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


kthLN = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)

###

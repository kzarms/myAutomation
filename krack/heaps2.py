class MaxHeap():

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = 2**30
        self.Front = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2*pos

    def rightChild(self, pos):
        return 2*pos + 1

    def isLeaf(self, pos):
        if (pos >= (self.size//2)) and (pos <= self.size):
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)]) or (self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size//2 + 1)):
            print("Parent: " + str(self.Heap[i]) +
                  " Lef Ch: " + str(self.Heap[2*i]) +
                  " Rgh Ch: " + str(self.Heap[2*i + 1]))

    def extractMax(self):
        poped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.Front)

        return poped


maxHeap = MaxHeap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)

maxHeap.Print()


# K largest elements in the array #
from heapq import *

arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k = 3

def findKlarg(arr, k):
    minHeap = []
    heappush(minHeap, arr[0])

    for i in range(1, len(arr)):
        if len(minHeap) < k:
            heappush(minHeap, arr[i])
        else:
            if minHeap[0] < arr[i]:
                heappushpop(minHeap, arr[i])

    return minHeap


print(findKlarg(arr, k))

def findKsmall(arr, k):
    heapify(arr)
    result = []
    for i in range(k):
        x = heappop(arr)
        result.append(x)

    return result

print(findKsmall(arr, k))


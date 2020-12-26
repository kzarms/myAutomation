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

########################
from heapq import *


arr = [2, 4, 5, 6, 9, 13, 15]
k = 3
x = 6

def find_closest_element(arr, k, x):
    result = []

    def binS(arr, x, start, end):

        mid = int((start + end) / 2)

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            return binS(arr, x, mid+1, end)
        else:
            return binS(arr, x, start, mid-1)

    index = binS(arr, x, 0, 5)

    for i in range(index - 2, index + 3):
        heappush(result, arr[i])

    return result[0:3]

print(find_closest_element(arr, k, x))


#### Summ of two values

A = [2, 7, 11, 15]
val = 9

def find_sum_of_two(A, val):
    h = {}
    for i in range(len(A)):
        x = val - A[i]
        if x in h:
            return h[x], i
        else:
            h[A[i]] = i
    return None


print(find_sum_of_two(A, val))


### Delete node with a given key

head = [4, 5, 1, 9]
key = 5

def delete_node(head, key):
    prev = 0
    if key == head[0]:
        return head[1:]

    for i in range(len(head)):
        if head[i] == key:
            return head[0:prev + 1] + head[i + 1:]
        else:
            prev = i
    return head

print(delete_node(head, key))

a = 400
b = 400
id(a) == id(b)




a = 4
b = 4
id(a) == id(b)

# https://www.educative.io/blog/google-coding-interview-questions

a = [1, 2]
b = a[:]

id(a)
id(b)

# Mirror binary tree nodes

tree = [40, 100, 400, 150, 50, 300, 600]


class node():
    def __init(self, data):
        self.left = None
        self.right = None
        slef.data = data

    def inOrder(root):
        if root:
            inOrder(root.left)
            print(root.data)
            inOrder(root.right)

    def mirror(root):
        if root:
            mirror(root.left)
            mirror(root.right)
            root.left, root.right = root.right, root.left


def mirror_tree(tree):
    result = []

    return result

#######


def valid_number(x):
    l = x.split(".")
    if len(l) == 1:
        if l[0].isnumeric():
            return True
    elif len(l) == 2:
        if l[0].isnumeric() and l[0].isnumeric():
            return True

    return False


x = "345"
print(valid_number(x))

x = "34.54"
print(valid_number(x))

x = "22.33.22"
print(valid_number(x))

x = ".33"
print(valid_number(x))


arr = [8, 3, 5, 2, 4, 6, 0, 1]

def find_missing_num(arr):
    # Find number about array
    act_sum = sum(arr)
    exp_sum = sum(range(len(arr)+1))
    return exp_sum - act_sum

print(find_missing_num(arr))

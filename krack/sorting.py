## Selection sort n^2

arr = [64, 25, 12, 22, 11]

# My
def selectSort(arr):
    result = []
    temp_arr = arr[:]
    for i in range(len(temp_arr)):
        minVal = min(temp_arr)
        result.append(minVal)
        temp_arr.remove(minVal)
    return result


print(selectSort(arr))

# Example


def selectSort2(arr):
    for i in range(len(arr)):
        # Manual look for a min value
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selectSort2(arr))

# Bubble sort n^2
# My implementation

arr = [64, 34, 25, 12, 22, 11, 90]


def myBubbleSort(arr):
    temp_arr = arr[:]
    swipe = True
    while swipe:
        swipe = False
        for i in range(len(temp_arr) - 1):
            if temp_arr[i] > temp_arr[i + 1]:
                swipe = True
                temp_arr[i], temp_arr[i + 1] = temp_arr[i + 1], temp_arr[i]
    return temp_arr


print(myBubbleSort(arr))

# Optimized implementation with two loops


def bubbleSort(arr):
    temp_arr = arr[:]
    n = len(temp_arr)

    for i in range(n):
        # last i elements are in plase already
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]

    return temp_arr


print(bubbleSort(arr))


def bubbleSortRec(arr):
    n = len(arr)

    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubbleSortRec(arr[:-1])


bubbleSortRec(arr)

arr = [64, 34, 25, 80, 12, 22, 11]

# Insertion sort


def insertionSort(arr):
    temp_arr = arr[:]

    for i in range(1, len(temp_arr)):
        key = temp_arr[i]
        j = i - 1
        while j >= 0 and key < temp_arr[j]:
            temp_arr[j + 1] = temp_arr[j]
            j -= 1
        temp_arr[j + 1] = key
    return temp_arr


print(insertionSort(arr))


#### Merge sort!
# First of all device and couquer


def dac_max(arr, index, lenth):
    max = -1
    if index >= lenth - 2:
        if arr[index] > arr[index + 1]:
            return arr[index]
        else:
            return arr[index + 1]
    max = dac_max(arr, index + 1, lenth)

    if arr[index] > max:
        return arr[index]
    else:
        return max


print(dac_max(arr, 0, 7))


def dac_min(arr, index, lenth):
    min = 0

    if index >= lenth - 2:
        if arr[index] > arr[index + 1]:
            return arr[index]
        else:
            arr[index + 1]

    min = dac_min(arr, index + 1, lenth)

    if arr[index] < min:
        return arr[index]
    else:
        return min


print(dac_min(arr, 0, 7))


# merge sort
arr = [64, 34, 25, 80, 12, 22, 11]


def mergSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergSort(L)
        mergSort(R)

        i = j = k = 0

        while (i < len(L)) and (j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


mergSort(arr)
print(arr)


def myMS(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        L = arr[:m]
        R = arr[m:]

        myMS(L)
        myMS(R)

        i = j = k = 0
        while (i < len(L)) and (j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [64, 34, 25, 80, 12, 22, 11]
myMS(arr)
print(arr)


############ Merge iterative

def msi(arr):
    size = 1
    while size < (len(arr) - 1):
        left = 0
        while left < len(arr) - 1:
            mid = min((size + left -1), (len(arr) - 1))
            right = min((size*2 + left -1), (len(arr) - 1))

            merge(arr, left, mid, right)
            left = left + size*2
        size = 2*size

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = arr[l + i]
    for i in range(n2):
        R[i] = arr[m + i + 1]

    i, j, k = 0, 0, l
    while (i < n1) and (j < n2):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [64, 34, 25, 80, 12, 22, 11]
msi(arr)
print(arr)


# Quick sort

def part(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = part(arr, low, high)

        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

arr = [64, 34, 25, 80, 12, 22, 11]
quicksort(arr, 0, 7 - 1)
print(arr)


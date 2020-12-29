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

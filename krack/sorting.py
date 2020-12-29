## Selection sort

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
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selectSort2(arr))



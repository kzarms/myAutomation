###### Sum of a bit difference #########

arr = [1, 2]

def sumBitDiff(arr):

    result = 0

    for i in range(16):
        count = 0
        for j in range(len(arr)):
            if arr[j] & (1 << i):
                count += 1
        result += count * 2

    return result

print(sumBitDiff(arr))





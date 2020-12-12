# Selection sort
arr = [5, 3, 4, 6, 16, 54, 23, 2, 44, 57, 65, 34]

# d = dict(enumerate(arr,1))
# rd = {v:k for k,v in d.items()}


def SelectionSort(arr):
    result = []
    while arr:
        myMin = arr[0]
        for i in arr:
            if i < myMin:
                myMin = i
        result.append(myMin)
        arr.remove(myMin)
    return result


print(SelectionSort(arr))

arr = [2, 4, 6]


def recSum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recSum(arr[1:])


print(recSum(arr))


### Qucick sort ###
arr = [5, 3, 4, 6, 16, 54, 23, 2, 44, 57, 65, 34]


def myQsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return myQsort(less) + [pivot] + myQsort(greater)


print(myQsort(arr))

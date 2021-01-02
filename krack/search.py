### Liniar search ###

arr = [10, 20, 30, 80, 50, 70, 40, 90]
x = 80

def lsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(lsearch(arr, x))
print(lsearch(arr, 60))


## BTS ###

arr = [2, 3, 4, 10, 40, 50, 55, 70, 75, 80, 91, 94, 99]

def binSearch(arr, x):

    l = arr[0]
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

print(binSearch(arr, 10))
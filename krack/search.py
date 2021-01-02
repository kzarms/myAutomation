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

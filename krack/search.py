### Liniar search ### O(n)

arr = [10, 20, 30, 80, 50, 70, 40, 90]
x = 80

def lsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(lsearch(arr, x))
print(lsearch(arr, 60))


## BTS ### O(log(n))

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


#### jump search ##### O(sqrt(n))
arr = [2, 3, 4, 10, 40, 50, 55, 70, 75, 80, 91, 94, 99, 101, 123, 144]

def jsearch(arr, x):

    jump = int(len(arr)**(1/2))
    i = 0
    while i <= (len(arr) -1) and arr[i] <= x:
        if arr[i] == x:
            return i
        elif arr[i] < x:
            i = i + jump
        else:
            break

    # i has the index of value > than x
    for j in range(i, i - jump, -1):
        if arr[j] == x:
            return j

    return -1

print(jsearch(arr, x))

### interpol search ###

def interpolS(arr, lo, hi, x):

    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        pos = lo + ((x - arr[lo])*(hi - lo)//(arr[hi] - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolS(arr, pos+1, hi, x)
        else:
            return interpolS(arr, lo, pos-1, x)
    return -1

print(interpolS(arr, 0, 15, 10))



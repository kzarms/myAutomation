####### Ugly numbers ########


def getNthUglyNo(n):

    ugly = [0] * n
    ugly[0] = 1

    i2 = i3 = i5 = 0

    next2 = 2
    next3 = 3
    next5 = 5

    for i in range(1, n):
        ugly[i] = min(next2, next3, next5)

        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5] * 5

    return ugly[-1]


n = 150
print(getNthUglyNo(n))

###### Catalan number #######

n = 5


def catNum(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catNum(i) * catNum(n - i - 1)

    return res


print(catNum(n))


def dynCatNum(n):
    if n == 0 or n == 1:
        return 1

    catalan = [0 for i in range(n + 1)]

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j]
            catalan[i] *= catalan[i - j - 1]

    return catalan[n]


print(dynCatNum(5))


# Binomical coefficient

def catalanB(n, k):
    if k > (n - k):
        k = n - k

    res = 1

    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res

def catBin(n):
    return int(catalanB(2*n, n)/(n +1))

print(catBin(5))



###### Gold meiner #######

mat = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]

len(mat[0])


def gold(mat):

    m = len(mat)
    n = len(mat[0])

    goldTable = [[0 for i in range(n + 1)] for j in range(m)]

    for col in range(n):
        for row in range(m):
            if col == n:
                right = 0
            else:
                right = mat[row][col]

            if row == 0 or col == n:
                right_up = 0
            else:
                right_up = mat[row - 1][col]

            if row == (m - 1) or col == n:
                right_dw = 0
            else:
                right_dw = mat[row + 1][col]

            goldTable[row][col+1] = goldTable[row][col] + max(right, right_up, right_dw)

    res = goldTable[0][3]
    for i in range(m):
        res = max(res, goldTable[i][3])

    return res

print(gold(mat))

##### Conis ######

def counts(arr, n):

    m = len(arr)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            x = table[i - arr[j]][j] if i - arr[j] >= 0 else 0

            y = table[i][j-1] if j >= 1 else 0

            table[i][j] = x + y
    return table[n][m-1]


arr = [1, 2, 3]
n = 4

print(counts(arr, n))

#### Subset sum problem ######

arr = [3, 34, 4, 12, 5, 2]
x = 9

def subset(arr, x):
    n = len(arr)
    table = [[False for i in range(x + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        table[i][0] = True

    #for i in range(1, x + 1):
    #     table[0][i]= False

    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if j < arr[i-1]:
                table[i][j] = table[i-1][j]
            if j >= arr[i-1]:
                table[i][j] = table[i-1][j] or table[i-1][j - arr[i-1]]

    return table[n][x]

print(subset(arr, x))



def subSet2(arr, x):
    results = []

    def find(subArr, x, path=()):
        if not subArr:
            return
        if subArr[0] == x:
            results.append(path + (subArr[0],))
        else:
            find(subArr[1:], x - subArr[0], path + (subArr[0],))
            find(subArr[1:], x, path)
    find(arr, x)
    return results

print(subSet2(arr, x))


##### Number of steps #####

memo = {}

def stepsCount(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        if memo[n] > -1:
            return memo[n]

    memo[n] = stepsCount(n - 1, memo) + stepsCount(n - 2, memo) + stepsCount(n - 3, memo)

    return memo[n]

print(stepsCount(12, memo))

# Magic index #

arr = [-1, 0, 1, 2, 2, 2, 3, 3, 3, 4]

def getMindex(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

def getMindex2(arr, s, e):
    if s == e:
        if arr[s] == s:
            return s
        else:
            return -1

    mid = (e - s)//2
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid:
        return getMindex2(arr, s, mid)
    else:
        return getMindex2(arr, mid, e)



print(getMindex2(arr, 0, len(arr)-1))

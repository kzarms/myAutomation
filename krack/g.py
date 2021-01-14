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

######## Modular exponent ##############


x = 2
y = 3
p = 5

91 % 5
91 * 3 % 5


def foo(x, y, p):
    return (x**y) % p

print(foo(2, 3, 5))

def foo2(x, y, p):
    # (ab) % mod p = ((a mod p)(b mod p)) mod p
    res = 1
    modX = x % p
    while y > 0:
        if y & 1:
            res = (res * modX) % p
        y = y // 2
        modX = (modX * modX) % p

    return res


print(foo2(2, 3, 5))

####### Find the largest word in dict ###########

myDic = ["ale", "apple", "monkey", "plea"]
mySrt = "abpcplea"


def findLargestWord(myDic, myStr):

    basicHash = {}
    for i in myStr:
        if i in basicHash:
            basicHash[i] += 1
        else:
            basicHash[i] = 1

    maxVal = 0
    for el in myDic:
        tempHash = basicHash.copy()
        count = 0
        for i in el:
            if i in tempHash:
                if tempHash[i] == 0:
                    count = 0
                    break
                tempHash[i] -= 1
                count += 1
            else:
                count = 0
                break
        if maxVal < count:
            maxVal = count
    return maxVal

print(findLargestWord(myDic, mySrt))



def constructString(dp, n, bCnt=1, cCnt=2):
    if bCnt < 0 or cCnt < 0:
        return 0

    if n == 0:
        return 1
    if bCnt == 0 and cCnt == 0:
        return 1

    if dp[n][bCnt][cCnt] != -1:
        return dp[n][bCnt][cCnt]

    res = constructString(dp, n-1, bCnt, cCnt)
    res += constructString(dp, n-1, bCnt-1, cCnt-1)
    res += constructString(dp, n-1, bCnt, cCnt-1)

    dp[n][bCnt][cCnt] = res

    return dp[n][bCnt][cCnt]

def contSrt(n):
    dp = [[[-1 for x in range(n+2)] for y in range(3)] for z in range(4)]
    return constructString(dp, n)

print(contSrt(3))


################# O(1) #################
# https://careercup.appspot.com/question?id=5717453712654336

def contSrt2(n):

    res = 0
    # C = 0
    res += 1 # no B
    res += n # B on each position
    # C = 1
    res += 1 * n
    res += (n - 1)*n

    # C = 2
    res += 1*(n-1)*n/2
    res += (n-2)*(n*(n-1)/2)

    return res

print(contSrt2(3))


############ find triplets in the array ###################

arr = [0, -1, 2, -3, 1]

def findtrpl(arr):
    result = []
    n = len(arr)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(i + 2, n):
                temp = [arr[i], arr[j], arr[k]]
                if sum(temp) == 0:
                    result.append(temp)

    return result

print(findtrpl(arr))


def findtriplSort(arr):
    result = []

    n = len(arr)
    arr.sort()

    for i in range(n - 1):
        l = i + 1
        r = n - 1
        x = arr[i]

        while l < r:
            temp = [arr[l], x, arr[r]]
            if sum(temp) == 0:
                result.append(temp)
                l += 1
                r -= 1
            elif sum(temp) < 0:
                l += 1
            else:
                r -= 1
    return result

print(findtriplSort(arr))


# find selebrity #

matrix = [
    [ 0, 0, 1, 0 ],
    [ 0, 0, 1, 0 ],
    [ 0, 0, 0, 0 ],
    [ 0, 0, 1, 0 ]
]

def findSel(martix):

    s = []

    for i in range(len(matrix)):
        s.append(i)

    A = s.pop()
    B = s.pop()

    while len(s) > 1:
        if martix[A][B]:
            A = s.pop()
        else:
            B = s.pop()

    if len(s) == 0:
        return -1

    C = s.pop()

    if matrix[C][A]:
        C = A

    if matrix[C][B]:
        C = B

    for i in range(len(matrix)):
        if i != C and (martix[C][i] or (not martix[i][C])):
            return -1

    return C

print(findSel(matrix))

############ Strin is in to others ###########

def isInterleaved(a, b, c):

    col = len(a)
    row = len(b)

    if (col + row) != len(c):
        return False

    table = [ [False for i in range(col + 1)] for j in range(row + 1)]

    for i in range(row + 1):
        for j in range(col + 1):

            if i == 0 or j == 0:
                table[i][j] = True

            # C[i] match to a but not to B
            elif (a[i - 1] == c[i + j - 1] and
                  b[j - 1] != c[i + j - 1]):
                table[i][j] = table[i - 1][j]

            # C[i] mathc to b but not to A
            elif (a[i - 1] != c[i + j - 1] and
                  b[j - 1] == c[i + j - 1]):
                table[i][j] = table[i][j - 1]

            # match both
            elif (a[i - 1] == c[i + j - 1] and
                  b[j - 1] == c[i + j - 1]):
                table[i][j] = table[i - 1][j] or table[i][j - 1]

    return table[col][row]

print(isInterleaved("XY", "WZ", "WZXY"))



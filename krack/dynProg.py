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

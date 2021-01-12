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





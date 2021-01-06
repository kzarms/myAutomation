### Insetrtion ###


a = bin(15)[2:]

N = '10000000000'
M = '10011'
j = 6

def insert(N, M, j):

    n = int(N, 2)
    m = int(M, 2)
    mj = m << j
    return bin(n + mj)[2:]

print(insert(N, M, 2))

n = bin(1775)[2:]

arr = n.split('0')
arr

for i in range(1, len(arr)):
    max = 0
    summ = len(arr[i-1]) + len(arr[i])
    if summ > max:
        max = summ

max += 1


a = '11101'
b = '01111'

flip = 0
for i in range(len(a)):
    if a[i] != b[i]:
        flip += 1

print(flip)

arr = [2, 5, 2, 8, 5, 6, 8, 8]

def printNumbers(arr):
    h = {}
    for i in range(len(arr)):
        if arr[i] in h:
            h[arr[i]] += 1
        else:
            h[arr[i]] = 1




################ Sum of Series ###############

def SofS(num):

    res = 0
    fact = 1

    for i in range(1, num + 1):
        fact *= i
        res = res + i/fact
    return res

print(SofS(5))




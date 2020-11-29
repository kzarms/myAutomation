
arr = [4, 3, 1, 2]
i = 0
# arr = [1, 3, 5, 2, 4, 6, 7]


def minimumSwaps(arr):
    mycount = 0
    normalDic = dict(enumerate(arr,1))
    reversDic = {v:k for k,v in normalDic.items()}
    for i in normalDic:
        x = normalDic[i]
        if x!=i:
            propElement = reversDic[i]
            normalDic[propElement] = x
            reversDic[x] = propElement
            mycount += 1
    return mycount


print(minimumSwaps(arr))

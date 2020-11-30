a = [2, 4]
b = [16, 32, 96]

a = [3, 4]
b = [24, 48]

def getTotalX(a, b):
    result = []
    minb = min(b)
    sampleList = []
    i = max(a)
    x = min(a)
    count = 1
    while x <= minb:
        x = i*count
        if (x not in sampleList) and (x <= minb):
            sampleList.append(x)
        count += 1
    
    result = sampleList.copy()
    for i in sampleList:
        for k in a:
            if i%k != 0:
                if i in result:
                    result.remove(i)
        for j in b:
            if j%i != 0:
                if i in result:
                    result.remove(i)

    return len(result)

print(getTotalX(a, b))
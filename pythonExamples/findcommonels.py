a = [2, 2, 3, 3, 5]
b = [1, 3, 4, 5]

def findcommonB(a, b):
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i)
    print(*set(result))


def findcommonO(a, b):
    result = []
    i = j = 0
    while((i < len(a)) & (j < len(b))):
        if(a[i] == b[j]):
            result.append(a[i])
            i += 1
            j += 1
        elif (a[i] > b[j]):
            j += 1
        else:
            i += 1
    print(result)

findcommonO(a, b)



from collections import defaultdict
d = defaultdict(list)
myList = []

nLen, mLen = map(int, input().split())
for i in range(nLen):
    d[input()].append(i+1)

for i in range(mLen):
    myList.append(input())

for i in myList:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print(-1)



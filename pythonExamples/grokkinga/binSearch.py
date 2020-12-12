sList = list(range(1, 101))


def binSearch(a, sList):
    low = 0
    high = len(sList) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = int((low + high) / 2)
        guess = sList[mid]
        if a == guess:
            return mid, steps
        if guess > a:
            high = mid
        else:
            low = mid


print(binSearch(12, sList))

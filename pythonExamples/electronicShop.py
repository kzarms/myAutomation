b = 10
keyboards = [3, 1]
drives = [5, 2, 8]


def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()

    for i in range(len(keyboards)-1, 0, -1):
        if keyboards[i] < b:
            x = b - keyboards[i]
            for j in range(len(drives)-1, 0, -1):
                if x - drives[j] >= 0:
                    return keyboards[i] + drives[j]
    return -1

print(getMoneySpent(keyboards, drives, b))

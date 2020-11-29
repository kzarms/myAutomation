a = [1, 2, 3, 4, 5]
d = 2

def rotLeft(a, d):
    if len(a) == d:
        return print(*a)
    if d == 0:
        return print(*a)
    return print(*(a[d:] + a[:d]))

rotLeft(a, d)
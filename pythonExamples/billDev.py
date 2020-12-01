bill = [3, 10, 2, 9]
k = 1
b = 12

def bonAppetit(bill, k, b):
    del bill[k]
    x = b - int(sum(bill)/2)
    if x == 0:
        return "Bon Appetit"
    else:
        return x

print(bonAppetit(bill, k, b))

bill = [3, 10, 2, 9]
k = 1
b = 7

print(bonAppetit(bill, k, b))

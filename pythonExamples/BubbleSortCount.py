a = [3, 2, 1]

def countSwaps(a):
    myCount = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                myCount += 1
    print("Array is sorted in", myCount, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

countSwaps(a)

prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50

def maximumToys(prices, k):
    myCount = 0
    while k >= 0:
        k = k - min(prices)
        prices.remove(min(prices))
        if k >= 0:
            myCount += 1
    
    return myCount

maximumToys(prices, k)


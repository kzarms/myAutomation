if __name__ == '__main__':
    ar = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ar.append([name, score])
    
    minValue = min(ar, key = lambda x: x[1])
    newAr = [x for x in ar if x[1] != minValue[1]]
    minValue2 = min(newAr, key = lambda x: x[1])
    newAr2 = [x for x in ar if x[1] == minValue2[1]]
    newAr2.sort()
    print('\n'.join([x[0] for x in newAr2]))
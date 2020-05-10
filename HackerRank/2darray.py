arr = []
s1 = '1 1 1 0 0 0'
s2 = '0 1 0 0 0 0'
s3 = '1 1 1 0 0 0'
s4 = '0 0 2 4 4 0'
s5 = '0 0 0 2 0 0'
s6 = '0 0 1 2 4 0'

arr.append(list(map(int, s1.split())))
arr.append(list(map(int, s2.split())))
arr.append(list(map(int, s3.split())))
arr.append(list(map(int, s4.split())))
arr.append(list(map(int, s5.split())))
arr.append(list(map(int, s6.split())))

def hourglassSum(arr):
    sumArr = []
    for i in range(4):
        for j in range(4):
            sumArr.append(sum(arr[i][j:(j+3)]) + (arr[i+1][j+1]) + sum(arr[i+2][j:(j+3)]))
    return max(sumArr)



print(hourglassSum(arr))
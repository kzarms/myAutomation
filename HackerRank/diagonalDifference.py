#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    lDiag = 0
    rDiag = 0
    for i in range(len(arr)):
        lDiag += arr[i][i]
        rDiag += arr[(len(arr)-i-1)][i]
    return abs(lDiag - rDiag)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    #arr = []

    #for _ in range(n):
    #    arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

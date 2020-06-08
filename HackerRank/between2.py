#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
a = [1]
b = [72,48]

def getTotalX(a, b):
    # Write your code here
    totalLen = len(a) + len(b)
    myArray = []
    maxA = max(a)
    minB = min(b)

    for myi in range(maxA,minB+1):
        myCount = 0
        for i in a:
            for y in b:
                if (myi % i) == 0:
                    if (y % myi) == 0:
                        myCount += 1
                        if totalLen == myCount:
                            myArray.append(myi)
    print(len(myArray))


getTotalX(a,b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

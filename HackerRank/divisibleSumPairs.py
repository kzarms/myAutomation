#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    totalSum = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if ((ar[i] + ar[j]) % k) == 0:
                totalSum += 1
    return totalSum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # ar = list(map(int, input().rstrip().split()))
    n = 0
    ar = [1, 3, 2, 6, 1, 2]
    k = 3
    result = divisibleSumPairs(n, k, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

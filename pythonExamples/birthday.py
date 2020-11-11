#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    TotalCount = 0
    if m == 1:
        return s.count(d)

    for i in range(len(s)):
        if sum(s[i:(i+m)]) == d:
            TotalCount += 1
    return TotalCount

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # dm = input().rstrip().split()

    # d = int(dm[0])

    # m = int(dm[1])
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2

    s = [4]
    d = 4
    m = 1

    s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
    d = 18
    m = 7

    result = birthday(s, d, m)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

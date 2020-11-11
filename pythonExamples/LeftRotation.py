#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # if d == 0:
    #     return a
    # d += -1
    # b = a[1::]
    # b.append(a[0])
    # return rotLeft(b, d)
    b = a[d::]
    for i in range(d):
        b.append(a[i])
    return b



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])

    # d = int(nd[1])

    # a = list(map(int, input().rstrip().split()))
    d = 4
    s = '1 2 3 4 5'
    a = list(map(int, s.split()))

    result = rotLeft(a, d)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

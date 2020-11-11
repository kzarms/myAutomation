#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar2 = ar.copy()
    countpair = 0
    for x in ar:
        countpair += ar2.count(x) // 2
        while x in ar2:
            ar2.remove(x)
    return countpair

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    n = 0
    s = '10 20 20 10 10 30 50 10 20'
    ar = list(map(int, s.split()))
    #ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

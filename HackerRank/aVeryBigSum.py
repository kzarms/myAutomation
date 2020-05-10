#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for el in ar:
        sum += el
    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ar_count = int(input())

    #ar = list(map(int, input().rstrip().split()))

    #ar_count = 5
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    
    result = aVeryBigSum(ar)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

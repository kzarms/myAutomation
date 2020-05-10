#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxvalue = max(ar)
    return ar.count(maxvalue)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ar_count = int(input())

    #ar = list(map(int, input().rstrip().split()))
    ar= [3,2,1,3]

    result = birthdayCakeCandles(ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

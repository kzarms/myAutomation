#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    jump=0
    for i in c:
        if i==0:
            count+=1
        else:
            jump=jump+count//2+1
            count=0
    if count>1:
        jump=jump+count//2
    return jump

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #c = list(map(int, input().rstrip().split()))
    s = '0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 0 1 0'
    c = list(s.split())
    #c = [0, 0, 1, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

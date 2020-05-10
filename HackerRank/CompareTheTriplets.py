#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    i = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        if a[i] < b[i]:
            bob += 1
    
    return [alice,bob]






if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = list(map(int, input().rstrip().split()))

    #b = list(map(int, input().rstrip().split()))
    a = [1,2,3]
    b = [2,2,2]
    result = compareTriplets(a, b)

    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

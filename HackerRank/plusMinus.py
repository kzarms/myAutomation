#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    UperZero = 0    
    JustZero = 0
    DownZero = 0

    for x in arr:
        if (x > 0):
           UperZero += 1
        if (x == 0):
            JustZero += 1
        if (x < 0):
            DownZero += 1
    print(str(UperZero/len(arr)))
    print(str(DownZero/len(arr)))
    print(str(JustZero/len(arr)))

if __name__ == '__main__':
    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)

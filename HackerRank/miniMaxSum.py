#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    MinSumm = 0
    MaxSumm = 0
    if(min(arr) == max(arr)):
        MySumm = sum(arr)-arr[0]
        print(MySumm, MySumm)
        return

    for i in arr:
        if(i == min(arr)):
            MinSumm += i
        elif(i == max(arr)):
            MaxSumm += i
        else:
            MinSumm += i
            MaxSumm += i
    print(MinSumm, MaxSumm)



if __name__ == '__main__':
    #arr = list(map(int, input().rstrip().split()))
    arr = [1,2,3,4,5]
    miniMaxSum(arr)


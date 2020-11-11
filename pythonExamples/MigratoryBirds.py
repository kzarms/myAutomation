#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
arr = [1, 4, 4, 4, 5, 3]
def migratoryBirds(arr):
    myArr = [arr.count(1),arr.count(2),arr.count(3),arr.count(4),arr.count(5)]
    return myArr.index(max(myArr))+1

print(migratoryBirds(arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

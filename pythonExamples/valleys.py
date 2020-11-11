#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    belowCount = 0
    attitudeIndex = 0

    for x in s:
        if x == 'U':
            if (attitudeIndex + 1) == 0:
                belowCount += 1
            attitudeIndex += 1            
        else:
            attitudeIndex += -1
    return belowCount



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #s = input()
    s = 'UDDDUDUU'
    n = 0
    result = countingValleys(n, s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
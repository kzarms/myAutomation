#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    aList = []
    bList = []
    CommonValue = 0
    for x in a:
        aList.append(x)
    for x in b:
        bList.append(x)
    aListCopy = aList.copy()
    for x in aList:
        if (x in bList) and (x in aListCopy):
            bList.remove(x)
            aListCopy.remove(x)
            CommonValue += 1
    return (len(a)-CommonValue + len(b)-CommonValue)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = input()

    # b = input()
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)
    print(res)
    #fptr.write(str(res) + '\n')

    #fptr.close()
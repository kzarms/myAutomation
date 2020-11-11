#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #generate string
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = 'a'
    n = 1000000000000
    #n = int(input())

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


def findN(n):
    if n == 1:
        return 1

    s = bin(n)[2::]
    return len(max(s.split('0')))

if __name__ == '__main__':
    n = int(input())
    print(findN(n))


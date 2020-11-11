import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sumResult = 0
    for x in ar:
        sumResult += x
    return sumResult

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ar_count = int(input())

    #ar = list(map(int, input().rstrip().split()))
    ar = [1, 2, 3, 4, 10, 11]
    result = simpleArraySum(ar)
    print(result)
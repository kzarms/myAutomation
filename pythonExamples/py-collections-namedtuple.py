from collections import namedtuple

n = int(input().rstrip())
student = namedtuple('student', input())
total = 0


for _ in range(n):
    total += int(student(*input().split()).MARKS)

print('{:.2f}'.format(total/n))

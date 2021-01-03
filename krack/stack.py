### Stack with pop, push and min with O(1)









class myStack:
    def __init__(self):
        self.min = None
        self.vals = []    # creates a new empty list for each dog

    def push(self, val):
        self.vals.append(val)

        if not self.min:
            self.min = val
        else:
            if self.min > val:
                self.min = val

    def pop(self):
        self.vals.pop()

    def __repr__(self):
        return "".join(str(self.vals)) + f" min is {self.min} "




s = myStack()

s.push(6)
s.push(3)
s.push(4)


s = '*-A/BC-/AKL'


def pefix(s):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    s = s[::-1]
    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b+i)
        else:
            stack.append(i)
    print(stack)

pefix(s)


def spanCalc(price, n, S):

    S[0] = 1

    for i in range(1, n):
        S[i] = 1
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1
    print(S)

price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

spanCalc(price, n, S)


def calcSpan2(price):

    n = len(price)
    S = [0 for x in range(n)]
    S[0] = 1

    stack = []
    stack.append(0)

    for i in range(1, n):
        while len(stack) > 0 and price[stack[-1]] <= price[i]:
            stack.pop()
        S[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])
        stack.append(i)

    print(S)

calcSpan2(price)


####### Next greater element ##########

arr = [11, 13, 21, 3, 17, 22, 8, 1]
def nge(arr):
    result = []
    for i in range(0, len(arr)):
        next = -1
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        result.append(next)

    print(result)

nge(arr)


def nge2(arr):
    stack = []
    stack.append(arr[0])
    result = []

    for i in range(1, len(arr)):
        next = arr[i]

        if len(stack) > 0:
            el = stack.pop()
            while el < next:
                result.append([el, next])
                if len(stack) == 0:
                    break
                el = stack.pop()
            if el > next:
                stack.append(el)

        stack.append(next)
    while len(stack) > 0:
        el = stack.pop()
        result.append([el, -1])

    print(result)

nge2(arr)

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


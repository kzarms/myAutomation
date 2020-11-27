from collections import deque

class book:
    def __init__(self, pages):
        self.pages = pages
    def size(self):
        print("This book has", self.pages, "pages!")


dog = book(10)


myStack = deque()

myStack.append("a")
myStack.append("b")

myStack
a = "".join(myStack)
class node:
    def __init__(self, data):

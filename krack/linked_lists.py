class ListNode:
    # Define a node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return "yo"

class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        # Insert a new element in the beginning
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        # add an element in the end
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def get(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return nodes

    def revers(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


my_list = LinkedList()

my_list.append("a")
my_list.append("b")
my_list.prepend("c")
my_list.append("c")
#my_list.remove("b")

my_list

a = LinkedList()
a.append(7)
a.append(1)
a.append(6)

b = LinkedList()
b.append(5)
b.append(9)
b.append(2)

def sumList(a, b):
    temp_a = a.get()[::-1]
    temp_b = b.get()[::-1]

    sum = int("".join(temp_a)) + int("".join(temp_b))
    sumL = list(str(sum))[::-1]
    c = LinkedList()
    for el in sumL:
        c.append(int(el))

    return c

print(sumList(a, b))

def sumList2(a, b):
    c = LinkedList()
    register = 0
    for i, j in zip(a.get(), b.get()):
        sum = int(i) + int(j)
        c.append(sum % 10 + register)
        register = 0
        if sum > 9:
            register = 1
    return c


print(sumList2(a, b))


######### Revers linked list ##########

l = LinkedList()
l.append("a")
l.append("b")
l.append("c")
l.append("d")

print(l)
l.revers()

l.printList()




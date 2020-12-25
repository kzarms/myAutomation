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



my_list = LinkedList()

my_list.append("a")
my_list.append("b")
my_list.prepend("c")
my_list.append("c")
#my_list.remove("b")

my_list


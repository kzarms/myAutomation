arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree():

    def __init__(self):
        self.nodes = []

    def append(self, data):
        root = Node(data)

        if not self.nodes:
            self.nodes.append(root)



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


arr = [12, 2, 13, 4, 5, 7, 8, 6, 10, 9, 11, 1, 3]

class node():
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

    def __repr__(self):
        return str(self.data)

    def prn(self):
        if self.left:
            self.left.prn()
        print(self.data)
        if self.right:
            self.right.prn()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


tree = node()

for el in arr:
    tree.insert(el)
    tree.prn()


###### BFS ######

class Graph():

    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self, s):

        visited = [False]*(max(self.graph) + 1)
        q = []

        q.append(s)
        visited[s] = True

        while q:
            s = q.pop()
            print(s)

            for i in self.graph:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)


g.DFS(2)



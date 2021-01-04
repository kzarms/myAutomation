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
g.addEdge(0, 1)

############ TSP ###############

class Graph2():

    def __init__(self):
        self.graph = {}

    def addEdge(self, n, links):
        self.graph[n] = links

    def __repr__(self):
        return str(self.graph)

    def getNode(self, n):
        if n in self.graph:
            return self.graph[n]
        else:
            return -1
    def getCost(self, a, b):
        return self.graph[a][b]


citys = Graph2()
citys.addEdge(1, {2:10, 3:15, 4:20})
citys.addEdge(2, {1:10, 3:35, 4:25})
citys.addEdge(3, {1:15, 2:35, 4:30})
citys.addEdge(4, {1:20, 2:25, 3:30})


def permut(a, l, r):
    if l == r:
        return a
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permut(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


# print(permut(["a","b","c"], 0, 2))

import itertools

def brutForse(citys):
    routes = list(itertools.permutations([2,3,4]))
    trips = []
    for route in routes:
        trip = [1]
        trip = trip + list(route)
        trip.append(1)
        trips.append(trip)

    sumList = []
    for trip in trips:
        sum = 0
        for i in range(0, 4):
            sum += citys.getCost(trip[i], trip[i+1])
        sumList.append(sum)

    print(sumList)


brutForse(citys)




from collections import deque

graph = {}
graph["i"] = ["alice", "bob", "charli"]
graph["alice"] = ["kilo", "fockstrot"]
graph["bob"] = ["lena"]
graph["charli"] = ["kilo", "lena"]
graph["kilo"] = ["alice", "charli", "lena"]
graph["lena"] = ["kilo"]
graph["fockstrot"] = ["alice"]

search_q = deque()
search_q += graph["i"]

while search_q:
    person = search_q.popleft()
    if person[-1] == "a":
        print(person, "is a mango!")
        break
    else:
        search_q += graph[person]


############################ Greede algorithm ########################

a = set(["a", "b", "c"])
b = set(["c", "d", "f"])

a | b

a & b

a - b
b - a
a | b




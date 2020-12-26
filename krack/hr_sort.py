n = [
    ["amy", 100],
    ["david", 100],
    ["heraldo", 50],
    ["aakansha", 75],
    ["aleksa", 150]
]

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name + " " + str(self.score)

    def comparator(a, b):
        if a.score > b.score:
            return 1
        if a.score == b.score:
            if a.name > b.name:
                return 1
        return -1

p = Player("alice", 100)
p2 = Player("bob", 200)


###### Fraudulent Activity notification



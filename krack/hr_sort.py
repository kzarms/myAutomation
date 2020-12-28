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



def pageCount(n, p):
    a = (n-p)//2
    b = p//2

    min(p//2, (n-p)//2)

    return a if a < b else b



pageCount(6, 2)
pageCount(6, 5)

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

def getMoneySpent(keyboards, drives, b):
    mBudget = -1
    for i in keyboards:
        for j in drives:
            sumCost = i + j
            if sumCost <= b:
                if mBudget < sumCost:
                    mBudget = sumCost

    return mBudget


x = 1
y = 2
z = 3


sample = """22 75 70
33 86 59
47 29 89
18 19 82
84 17 18
100 11 55
37 57 75
47 30 6
40 68 50
26 37 31
93 49 20
84 78 31
80 57 86
57 94 55
21 80 4
1 68 67
74 91 23
85 66 80
21 95 58
86 69 77
31 2 46
45 94 99
7 66 36
63 34 33
75 92 65
90 45 54
12 9 10
43 56 51
92 20 56
97 12 67
17 38 86
85 94 20
6 81 53
77 27 54
62 25 37
56 70 63
49 32 16
4 61 39
92 30 61
41 59 81
100 66 83
16 16 16
81 70 30
11 33 22
35 98 18
43 62 48
84 54 69
73 72 86
34 82 49
16 83 62
57 50 53
36 49 88
5 80 42
20 86 47
43 40 41
72 12 42
16 43 29
11 35 23
12 63 37
84 78 55
17 90 78
28 10 84
39 96 67
22 84 53
49 77 63
77 82 55
17 53 35
79 31 55
7 56 31
2 7 4
99 82 60
20 17 18
1 98 49
91 66 13
95 23 1
87 59 73
10 10 56
61 54 59
62 94 78
49 29 37
87 79 83
72 1 42
42 34 38
52 82 98
29 12 43
81 50 97
80 17 43
88 38 40
41 55 84
48 91 69
11 74 23
84 68 76
4 51 80
51 85 39
37 74 55
15 65 54
57 14 56
43 61 56
9 79 35
4 44 44
"""

results = """Cat B
Cat A
Cat A
Cat B
Cat B
Cat B
Cat B
Cat B
Cat A
Cat A
Cat B
Cat B
Cat A
Cat A
Cat A
Cat B
Cat A
Cat A
Mouse C
Cat B
Cat A
Cat B
Cat A
Cat B
Cat A
Cat B
Cat B
Cat B
Mouse C
Cat A
Cat B
Cat A
Cat B
Cat A
Cat B
Mouse C
Cat B
Cat B
Mouse C
Cat B
Mouse C
Mouse C
Cat B
Mouse C
Cat A
Cat A
Mouse C
Cat A
Cat A
Cat B
Cat B
Cat B
Cat A
Cat A
Cat B
Mouse C
Cat A
Mouse C
Cat A
Cat B
Cat B
Cat A
Cat A
Mouse C
Mouse C
Cat A
Mouse C
Mouse C
Cat A
Cat A
Cat B
Cat B
Cat A
Cat B
Cat B
Mouse C
Mouse C
Cat A
Mouse C
Cat B
Mouse C
Cat A
Mouse C
Cat B
Cat A
Cat A
Cat B
Cat B
Cat B
Cat A
Cat A
Mouse C
Cat B
Cat A
Cat A
Cat B
Cat A
Cat B
Cat A
Cat B
"""



resultsl = results.splitlines()
samplel = sample.splitlines()

def catAndMouse(x, y, z):
    if x == y:
        return "Mouse C"
    if x > y:
        if z >= x:
            return "Cat A"
        if z <= y:
            return "Cat B"
    else:
        if z <= x:
            return "Cat A"
        if z >= y:
            return "Cat B"
    # Calc
    dist = abs(y-x)
    if dist/2 + min(x, y) == z:
        return "Mouse C"
    if x < y:
        if dist/2 + x < z:
            return "Cat B"
        else:
            return "Cat A"
    else:
        if dist/2 + y < z:
            return "Cat A"
        else:
            return "Cat B"


for i in range(len(samplel)):
    vals = samplel[i].split()
    check = catAndMouse(int(vals[0]), int(vals[1]), int(vals[2]))
    if check != resultsl[i]:
        print(i, vals, check)


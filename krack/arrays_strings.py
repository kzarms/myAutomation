# 1.1 is unique

u = "abcdefghijk"
s = "abcdeaghijk"


def isUnique(my_string):
    my_hash = {}

    for el in my_string:
        if el in my_hash:
            return "Not unique"
        else:
            my_hash[el] = 1
    return "Unique"


def isUniqueNoHash(my_string):
    for i in range(len(my_string)):
        if my_string[i] in my_string[i + 1 :]:
            return "Not unique"
    return "Unique"


def isUniqueSort(my_string):
    s_list = sorted(my_string)
    for i in range(len(s_list) - 1):
        if s_list[i] == s_list[i + 1]:
            return "Not unique"
    return "Unique"


print(isUnique(u))
print(isUnique(s))

print(isUniqueNoHash(u))
print(isUniqueNoHash(s))

print(isUniqueSort(u))
print(isUniqueSort(s))

# 1.2 Permutations
s1 = "abcd"
s2 = "acdb"
s3 = "acdf"


def isPerm(s1, s2):
    my_hash = {}

    for el in s1:
        if el in my_hash:
            my_hash[el] += 1
        else:
            my_hash[el] = 1

    for el in s2:
        if el in my_hash:
            my_hash[el] += -1
            if my_hash[el] < 0:
                return "Not perm"
        else:
            return "Not perm"
    return "Perm"


print(isPerm(s1, s2))
print(isPerm(s1, s3))

## 1.3 wright a method to replace all spaces with %20

s1 = "My name is Robot"
s2 = "My wrong example   "


def my_replace(s):
    wordList = s.rstrip().split(" ")
    return "%20".join(wordList)


print(my_replace(s1))
print(my_replace(s2))

# 1.4 Return a palindrom permutation of the string

s = "tact coa"
s2 = "tact coab"


def my_pp(s):
    my_hash = {}
    my_s = s.replace(" ", "")
    for el in my_s:
        if el in my_hash:
            my_hash[el] += 1
        else:
            my_hash[el] = 1

    odd = True if len(my_s) % 2 else False

    odd_count = 0
    for el in my_hash.keys():
        if my_hash[el] % 2:
            odd_count += 1
    if odd:
        if odd_count == 1:
            return "Polindrom"
        else:
            return "Not polindrom"
    else:
        if odd_count > 0:
            return "Not polindrom"
        else:
            return "Polyndrom"


print(my_pp(s))
print(my_pp(s2))


# 1.5 find a way how many chanses has been done:

s1 = "pale"
s2 = "ple"
s3 = "bake"

for i, j in zip(s1, s3):
    print(i, j)


def string_check(s, r):
    my_hash = {}

    if s == r:
        return "No change"

    if len(s) == len(r):
        # One replace
        # Put values in the array
        replace_count = 0
        for i in range(len(s)):
            if s[i] != r[i]:
                replace_count += 1
        if replace_count == 1:
            return "One replace, true"
        else:
            return "More than one replace, false"

    elif len(s) == len(r) + 1:
        # Insert a char in r
        pass

    elif len(s) == len(r) - 1:
        # Remove char in r
        pass

    else:
        return "Wrong"


print(string_check(s1, s2))
print(string_check(s1, s3))

# 1.6 manual zip function

s = "aabcccccaaa"


def my_zip(s):

    result = []
    restulStr = ""
    count = 0
    curr_char = s[0]
    for el in s:
        if el == curr_char:
            count += 1
        else:
            result.append((curr_char, count))
            count = 1
            curr_char = el
    # Finnal close
    result.append((curr_char, count))
    for el in result:
        restulStr += el[0] + str(el[1])
    if len(restulStr) >= len(s):
        return s
    else:
        return restulStr


print(my_zip(s))


# 1.7 Matrix rotation

m = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["j", "k", "l", "m"],
    ["n", "o", "p", "q"],
]


def my_rotate(m):
    # Rotate layer by layer
    new_m = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    matrix_len = len(m[0])
    layers = int(matrix_len / 2)
    for i in range(layers):
        first = i
        last = matrix_len - 1 - i
        for j in range(first, last):
            offset = j - first
            top = m[first][j]
            # left to top
            new_m[first][j] = m[last - offset][first]

            # bottom to left
            new_m[last - offset][first] = m[last][last - offset]

            # right to bottom
            new_m[last][last - offset] = m[j][last]

            # top to right
            new_m[j][last] = top

    return new_m


print(my_rotate(m))


# 1.8 set 0-s in the matrix

m = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["j", "k", "0", "m"],
    ["n", "o", "p", "q"],
]


def my_zero(m):

    row = []
    col = []

    size = len(m[0])
    for i in range(size):
        for j in range(size):
            if m[i][j] == "0":
                row.append(i)
                col.append(j)
    # Set nulls
    if row:
        for r in row:
            for i in range(size):
                m[r][i] = "0"
        for c in col:
            for j in range(size):
                m[j][c] = "0"
    return m


print(my_zero(m))

# 1.9 chech if string or not

s1 = "lainer"
s2 = "nerlai"


def my_rotation_check(s1, s2):
    sub = ""
    for i in s1:
        sub = sub + i
        if sub not in s2:
            sub = sub[:-1]
            break
    devider = len(sub) - 1
    return "yes" if s1[devider + 1 :] + s1[: devider + 1] == s2 else "No"


def my_rotation_check2(s1, s2):
    if len(s1) == len(s1) and len(s1) > 0:
        if s2 in s1 * 2:
            return "yes"
        if s1 in s2 * 2:
            return "yes"
    return "no"

print(my_rotation_check2("testblock", "blocktest"))
print(my_rotation_check2("testblock", "bolcktest"))

print(my_rotation_check(s1, s2))

print(my_rotation_check2(s1, s2))


# Find the closest pari between 2 sorted arrays.

a = [1, 4, 5, 7]
b = [10, 20, 30, 40]
x = 30

def findClosestPair(a, b, x):
    resultList = [x]
    myhash = {}
    for i in a:
        for j in b:
            s = i + j
            resultList.append(s)
            myhash[s] = [i, j]

    resultList.sort()
    index = resultList.index(x)

    l = x - resultList[index - 1]
    r = resultList[index + 1] - x

    if l < r:
        return myhash[resultList[index - 1]]
    else:
        return myhash[resultList[index + 1]]
print(findClosestPair(a, b, x))

def pclosest(a, b, x):

    i = 0
    j = len(b) - 1
    diff = 2**30

    while (i < len(a) and j >= 0 ):
        if abs(a[i] + b[j] - x) < diff:
            res_i = i
            res_j = j
            diff = abs(a[i] + b[j] - x)
        if a[i] + b[j] > x:
            j -= 1
        else:
            i += 1
    return a[res_i], b[res_j]

print(pclosest(a, b, x))



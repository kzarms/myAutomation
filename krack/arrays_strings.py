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
        if my_string[i] in my_string[i+1:]:
            return "Not unique"
    return "Unique"

def isUniqueSort(my_string):
    s_list = sorted(my_string)
    for i in range(len(s_list) - 1):
        if s_list[i] == s_list[i+1]:
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

def my_pp(s):
    print(s)


# 1.5 find a way how many chanses has been done:

s1 = "pale"
s2 = "ple"
s3 = "bake"

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

    elif len(s) == len(r)+1:
        # Insert a char in r
        insert_count = 0
        for i in range(len(s)):
            if s[i] != r[i]:
                insert_count += 1

    elif len(s) == len(r)-1:
        # Remove char in r
        pass

    else:
        return "Wrong"



print(string_check(s1, s2))

print(string_check(s1, s3))



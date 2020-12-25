magazine = "give me one grand today night"
note = "give one grand today"

def checkMagazine(magazine, note):
    hash = {}

    for w in magazine.split():
        if w in hash:
            hash[w] += 1
        else:
            hash[w] = 1

    for w in note.split():
        if w in hash:
            hash[w] += -1
            if hash[w] < 0:
                return "No"
        else:
            return "No"
    return "Yes"


checkMagazine(magazine, note)

magazine = "two times three is not four"
note = "two times two is four"
checkMagazine(magazine, note)

min(len(magazine), len(note))


# Complete the twoStrings function below.
s1 = "hello"
s2 = "banko"

def twoStrings(s1, s2):
    h = {}

    for el in s1:
        if el in h:
            h[el] += 1
        else:
            h[el] = 1
    for el in s2:
        if el in h:
            return "YES"
    return "NO"

def twoStrings2(s1, s2):
    return "YES" if set(s1)&set(s2) else "No"

print(twoStrings(s1, s2))
print(twoStrings2(s1, s2))


s = "abba"
s = 'ifailuhkqq'
def sherlockAndAnagrams(s):
    for i in range(len(s))
        pass


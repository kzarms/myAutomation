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



def sherlockAndAnagrams(s):
    anagrams = []
    h = {}
    summ = 0
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            anagrams.append("".join(sorted(s[j:j+i])))
    for el in anagrams:
        if el in h:
            h[el] += 1
        else:
            h[el] = 1
    for k in h.keys():
        if h[k] > 1:
            summ += sum(range(h[k]))
    return summ

sum(range(4))
s = "abba"
print(sherlockAndAnagrams(s))

s = 'ifailuhkqq'
print(sherlockAndAnagrams(s))

s = 'kkkk'
print(sherlockAndAnagrams(s))

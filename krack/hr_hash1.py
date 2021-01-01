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


####### Piking numbers ############

a = [4, 6, 5, 3, 3, 1]

a = [1, 1, 1, 1, 1]

def pickingNumbers(a):
    a.sort()

    longest = count = 0
    curr_min = a[0]

    for i in range(len(a)):
        if curr_min == a[i] or curr_min+1 == a[i]:
            count += 1
        else:
            if longest < count:
                longest = count
            curr_min = a[i]
            count = 1
    if longest < count:
        longest = count
    return longest

print(pickingNumbers(a))


#### Cliemb The leader board #####

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

def climbingLeaderboard(ranked, player):

    def rankCalc(ranked):
        current_rank = {}
        score = ranked[0]
        rank = 1
        for i in range(len(ranked)):
            if ranked[i] == score:
                if ranked[i] not in current_rank:
                    current_rank[ranked[i]] = rank
            else:
                rank += 1
                score = ranked[i]
                current_rank[ranked[i]] = rank
        return current_rank

    def rs(ranked):
        tempList = list(set(ranked))
        tempList.sort(reverse=True)
        h = {k:v for v,k in enumerate(tempList, 1)}
        return h

    runk_result = []
    rs = set(ranked)

    for i in range(len(player)):
        rs.add(player[i])

        runkList = rs(ranked)
        runk_result.append(runkList[player[i]])
        ranked.remove(player[i])

    return runk_result


print(climbingLeaderboard(ranked, player))


def climbingLeaderboard(scores,alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores)-1
    while score_index!=len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index>-1:
            highscore_index-=1
            if scores[highscore_index]!=scores[highscore_index+1]:
                currentrank-=1
        if alice[score_index] == scores[highscore_index]:
            yield currentrank
        else:
            yield currentrank+1
        score_index+=1

#s=input()
s = 'adfdfererfsdfsdf'
print(["".join(s[::2]),"".join(s[1::2])])

def myreplace(s, subs):
    return s.replace(subs,"")

myreplace(s, "df")

s.replace("df","!")


def mySreplace(s, subs):
    return "".join(s.split(subs))


for i in range(len(s)-1, -1, -1):
    print(i)

for i in range(len(s))[::-1]:
    print(s[i])

mylist = [pow(x,x) for x in range(5)]
[x*(x-1) for x in range(1,8)]
def perm(s):
    yield s

a, b = 5, 6
a, b = b, a
#lambda

x = lambda a: a + 1

print(x(5))
z = 4
print(lambda z: z*5)

'Yo {}'.format(z)

f"Hello {z}"



####################################################
#1
a = b = 5
id(a)
id(b)

a is b
c = 5
id(a)
id(c)
a is c
a = ["a"]
b = ["a"]

a is b
#2
"my test".istitle()
"My test".istitle()
"My Test".istitle()

#3
s = "my string is big"
"is" in s

#4
s.index("is")
s.find("is")

s.index("yo")
s.find("yo")

#5
len(s)

#6
s.count("i")

#7
s.capitalize()

#8
msg = "yo"
f"My test is {msg}"

#9
s.index("is",0,14)

#10
"My test is {}".format(msg)

#11 only digits
s.isnumeric()
"1234".isnumeric()
"+1234".isnumeric()
"12.34".isnumeric()

#12
s.split("is")
[x.strip() for x in s.split("is")]

#13
s.islower()

#14
s[0].islower()

#15
"a" + 5
"a"*5

#16
s[::-1]
"".join(reversed(s))

#17
l = ["a","b","c"]
"-".join(l)

#18
s.isascii()

#19
s.lower()
s.upper()

#20
s[0].upper() + s[1:-1] + s[-1].upper()

#21
"aA".isupper()
"AA".isupper()

#22
s1 = "abc\ndef"
s1.splitlines()

#23
s[3:8]

#24
str(4)

#25
"aBc".isalpha()
"aB2".isalpha()

#26
s.replace("i","1")

#27
min(s.replace(" ",""))

#28
s.isalnum()

"ab1".isalnum()
"a-1".isalnum()

#29
s.strip()

#30
s.startswith("my")
s.endswith("is")

#31
s.encode('ascii')
"123".encode('ascii')

#32
"   ".isspace()

#33
"abc"*3

#34
"a" + "b"

#35
s.partition("is")

#36
id(s)
id(s.replace("i","1"))

#37
a = "yo"
b = "yo"

id(a)
id(b)

#37

mapping = str.maketrans('abc',"123")
"a a bb cc".translate(mapping)

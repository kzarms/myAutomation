

n = int(input())
PhoneBook = {}
for i in range(n):
    pair = input().split()
    PhoneBook[pair[0]] = pair[1]


for i in range(n):
    query = input()
    if query in PhoneBook.keys():
        print(query,'=',PhoneBook[query],sep='')
    else:
        print('Not found')



if __name__ == '__main__':
    N = int(input())
a = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'insert':
        a.insert(int(cmd[1]), int(cmd[2]))
    if cmd[0] == 'remove':
        a.remove(int(cmd[1]))
    if cmd[0] == 'append':
        a.append(int(cmd[1]))
    if cmd[0] == 'sort':
        a.sort()
    if cmd[0] == 'pop':
        a.pop()
    if cmd[0] == 'reverse':
        a.reverse()
    if cmd[0] == 'print':
        print(a)

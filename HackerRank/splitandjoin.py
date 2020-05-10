def split_and_join(line):
    # write your code here
    return '-'.join(line.split(' '))

if __name__ == '__main__':
    #line = input()
    line = 'This is my line'
    result = split_and_join(line)
    print(result)
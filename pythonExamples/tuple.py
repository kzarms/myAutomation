
import builtins

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    #integer_list = [1, 2]
    print(hash(tuple(integer_list)))
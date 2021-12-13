import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = [-1] + list(map(int, input().split()))
L = len(_list)
T = int(input())
for _ in range(T):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, L, num):
            _list[i] = int(not _list[i])
    else:
        _list[num] = int(not _list[num])
        if num != 1:
            i = 1
            while True:
                if num - i < 1 and num + i > L:
                    break
                else:
                    
            
print(_list)

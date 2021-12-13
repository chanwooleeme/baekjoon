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
        i = 0
        cnt = 0
        while True:
            if i == 0:
                i = 1
                continue
            if 1 <= num - i and num + i < L:
                if _list[num - i] == _list[num + i]:
                    i += 1
                    cnt += 1
                else:
                    break
            else:
                break
        for j in range(num - cnt, num + cnt + 1):
            _list[j] = int(not _list[j])
        
_list = _list[1:]

i = 0
while i < len(_list) + 1:
    print(*_list[i:i + 20])
    i += 20
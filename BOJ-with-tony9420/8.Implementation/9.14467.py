import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
li = [-1]*11
cnt = 0
for _ in range(N):
    n, position = map(int, input().split())
    if li[n] != -1:
        if li[n] != position:
            li[n] = position
            cnt += 1
    else:
        li[n] = position
print(cnt)
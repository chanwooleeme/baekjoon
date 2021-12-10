import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
s = [-1] + list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        s[b] = c
    elif a == 2:
        for b in range(b, c+1):
            state = s[b]
            if state == 1:
                s[b] = 0
            else:
                s[b] = 1
    elif a == 3:
        for b in range(b, c+1):
            s[b] = 0
    elif a == 4:
        for b in range(b, c+1):
            s[b] = 1
print(*s[1:])

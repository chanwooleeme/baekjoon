import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

group = {}

for _ in range(N):
    group[input()] = True

cnt = 0
for _ in range(M):
    val = input()
    if val in group:
        cnt += 1
print(cnt) 
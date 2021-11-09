import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = deque([i + 1 for i in range(N)])
for _ in range(N - 1):
    q.popleft()
    q.rotate(-1)
print(q.popleft())
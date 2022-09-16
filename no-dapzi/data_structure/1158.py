import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, K = map(int, input().split())
    q = deque([x for x in range(1, N+1)])
    result = []
    while q:
        q.rotate(-K+1)
        result.append(q.popleft())
    print(''.join(str(result)).replace('[', '<').replace(']', '>'))
    return

solution()
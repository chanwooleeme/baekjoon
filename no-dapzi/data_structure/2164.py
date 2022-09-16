from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    q = deque([x for x in range(1, N+1)])
    result = -1
    while q:
        result = q.popleft()
        if q:
            q.rotate(-1)
    print(result)
    return

solution()
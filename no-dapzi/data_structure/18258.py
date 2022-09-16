import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    q = deque()
    for _ in range(N):
        s = input().split()
        if s[0] == 'push':
            q.append(int(s[1]))
        else:
            if not q:
                if s[0] == 'pop' or s[0] == 'front' or s[0] == 'back':
                    print(-1)
                elif s[0] == 'empty':
                    print(1)
                elif s[0] == 'size':
                    print(0)
            else:
                if s[0] == 'empty':
                    print(0)
                elif s[0] == 'size':
                    print(len(q))
                elif s[0] == 'pop':
                    print(q.popleft())
                elif s[0] == 'front':
                    print(q[0])
                elif s[0] == 'back':
                    print(q[-1])
                
    return

solution()
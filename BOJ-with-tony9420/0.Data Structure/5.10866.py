import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = deque()
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]
    if cmd == "push_front":
        q.appendleft(X)
    elif cmd == "push_back":
        q.append(X)
    elif cmd == "pop_front":
        if q:
        	print(q.popleft())
        else :
            print(-1)
    elif cmd == "pop_back":
        if q:
            print(q.pop())
        else :
            print(-1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == "back":
        if q :
            print(q[-1])
        else:
            print(-1)
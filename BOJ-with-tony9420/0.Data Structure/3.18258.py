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
    if cmd == "push":
        q.append(X)
    elif cmd == "pop":
        if not q:
            print("-1")
        else:
            print(q.popleft())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if not q:
            print("1")
        else:
            print("0")
    elif cmd == "front":
        if not q:
            print("-1")
        else:
            print(q[0])
    else:
        if not q:
            print("-1")
        else:
            print(q[-1])
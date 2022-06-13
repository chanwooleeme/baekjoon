from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = deque()

for _ in range(N):
    oprs = input().split()
    if oprs[0] == 'push':
        q.append(int(oprs[1]))
    else:
        opr = oprs[0]
        if opr == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif opr == 'size':
            print(len(q))
        elif opr == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif opr == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif opr == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
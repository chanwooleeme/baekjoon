import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    q = deque()
    for _ in range(N):
        oprs = input().split()
        if len(oprs) == 1:
            if oprs[0] == 'pop':
                if not q:
                    print(-1)
                else:
                    print(q.popleft())
            elif oprs[0] == 'front':
                if not q:
                    print(-1)
                else:
                    print(q[0])
            elif oprs[0] == 'back':
                if not q:
                    print(-1)
                else: print(q[-1])
            elif oprs[0] == 'size':
                print(len(q))
            elif oprs[0] == 'empty':
                if q:
                    print(0)
                else:
                    print(1)
        else:
            q.append(int(oprs[1]))

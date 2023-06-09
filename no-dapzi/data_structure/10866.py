from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
q = deque()
for _ in range(n):
    inputs = input().split(' ')
    opr, x = inputs[0], 0
    if len(inputs) != 1:
        x = inputs[1]
        if opr == 'push_front':
            q.appendleft(x)
        else:
            q.append(x)
    else:
        if opr == 'size':
            print(len(q))
        elif opr == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(q) == 0:
                print(-1)
            else:
                if opr == 'pop_front':
                    print(q.popleft())
                elif opr == 'pop_back':
                    print(q.pop())
                elif opr == 'size':
                    print(len(q))
                elif opr == 'front':
                    print(q[0])
                elif opr == 'back':
                    print(q[-1])

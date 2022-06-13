import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    is_error = False
    
    arr = list(filter(None,input()[1:-1].split(',')))
    q = deque()
    r = 0
    if arr:
        q = deque(int(x) for x in arr)
    for f in p:
        if f == 'R':
            if q:
                r += 1
        else:
            if q:
                if not r % 2:
                    q.popleft()
                else:
                    q.pop()
            else:
                is_error = True
                break
    if is_error:
        print("error")
    else:
        if r % 2:
            q = reversed(q)
        print(str(list(q)).replace(', ',','))
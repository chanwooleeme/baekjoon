import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    queue2 = deque()
    
    cnt = 1
    for i in range(len(arr)):
        queue.append(arr[i])
        queue2.append(i)
    while True:
        if max(queue) == queue[0]:
            if queue2[0] == M:
                print(cnt)
                break
            else:
                queue.popleft()
                queue2.popleft()
                cnt += 1
        else:
            queue.rotate(-1)
            queue2.rotate(-1)
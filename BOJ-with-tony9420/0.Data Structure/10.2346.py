import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int, input().split()))
queue = deque()
queue2 = deque()

for i in range(len(arr)):
    queue.append(i + 1)
    queue2.append(arr[i])

while queue2:
    val = queue2[0]
    if val > 0:
        queue2.popleft()
        queue2.rotate(-val + 1)
        print(queue.popleft())
        queue.rotate(-val + 1)
    else:
        queue2.popleft()
        queue2.rotate(-val)
        print(queue.popleft())
        queue.rotate(-val)
    
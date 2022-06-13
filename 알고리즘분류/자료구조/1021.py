from collections import deque
from copy import deepcopy
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
inputs = list(map(int, input().split()))

cnt = 0
for n in inputs:
    cnt1, cnt2 = 0,0
    tmp = deepcopy(q)
    while tmp[0] != n:
        tmp.rotate(-1)
        cnt1 += 1
    tmp = deepcopy(q)
    while tmp[0] != n:
        tmp.rotate(1)
        cnt2 += 1
    q = tmp
    q.popleft()
    cnt += min(cnt1, cnt2)
print(cnt)
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def transform_lst(lst):
    key_val_lst = []
    for idx, val in enumerate(lst):
        key_val_lst.append([idx, val])
    return key_val_lst


N = int(input())
lst = list(map(int, input().split()))
q = deque(transform_lst(lst))
result = []

while q:
    idx, cur = q.popleft()
    add_rotate = 1
    if cur < 0:
        add_rotate = 0
    q.rotate(cur * -1 + add_rotate)
    result.append(str(idx + 1))

print(' '.join(result))

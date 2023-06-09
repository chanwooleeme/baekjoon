import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def transform_q(lst):
    transformed_lst = []
    for i, val in enumerate(lst):
        transformed_lst.append([i, val])
    return deque(transformed_lst)


def printer(lst, M):
    result = 0
    q = transform_q(lst)
    sorted_lst = sorted(lst)
    while q:
        high_priority = sorted_lst[-1]
        key, val = q[0]
        if val == high_priority:
            q.popleft()
            sorted_lst.pop()
            result += 1
            if key == M:
                return result
        else:
            q.rotate(-1)

q = deque()
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print_lst = printer(lst, M)
    print(print_lst)

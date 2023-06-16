import sys
from collections import deque
from copy import deepcopy

def input():
    return sys.stdin.readline().rstrip()


def rotate(q, val, dir):
    tmp_q = deepcopy(q)
    cnt = 0
    while tmp_q[0] != val:
        tmp_q.rotate(dir)
        cnt += 1
    return tmp_q, cnt


if __name__ == '__main__':
    N, M = map(int, input().split())
    q = deque([i for i in range(1, N+1)])
    locs = list(map(int, input().split()))
    result = 0

    for i in range(len(locs)):
        val = locs[i]
        tmp_rq, right = rotate(q, val, -1)
        tmp_lq, left = rotate(q, val, 1)
        if left < right:
            q = tmp_rq
            result += left
        else:
            q = tmp_lq
            result += right
        q.popleft()
    print(result)

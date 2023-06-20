import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    q = deque()
    for i in range(N):
        if A[i] == 1:
            q.appendleft(i+1)
        elif A[i] == 2:
            tmp = q.popleft()
            q.appendleft(i+1)
            q.appendleft(tmp)
        else:
            q.append(i+1)
    print(" ".join(map(str, q)))
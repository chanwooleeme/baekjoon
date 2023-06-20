import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        P = input()
        N = int(input())
        X = input()
        is_r = False
        flag = False
        if N == 0:
            X = deque()
        else:
            X = deque(map(int, X[1:-1].split(',')))
        for i in range(len(P)):
            if P[i] == 'R':
                is_r = not is_r
            else:
                if not X:
                    print("error")
                    flag = True
                    break
                if is_r:
                    X.pop()
                else:
                    X.popleft()
        if not flag:
            if not is_r:
                print('['+','.join(map(str, X))+']')
            else:
                X.reverse()
                print('['+','.join(map(str, X))+']')

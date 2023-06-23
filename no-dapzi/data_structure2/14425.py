import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N, M = map(int, input().split())
    S_dict = dict()
    result = 0
    for _ in range(N):
        S_dict[input()] = True
    for _ in range(M):
        if input() in S_dict:
            result += 1
    print(result)
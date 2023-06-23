import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N, M = map(int, input().split())
    alpha_dict = dict()
    num_dict = dict()
    for i in range(N):
        s = input()
        alpha_dict[s] = str(i+1)
        num_dict[str(i+1)] = s
    for _ in range(M):
        s = input()
        if s.isalpha():
            print(alpha_dict[s])
        else:
            print(num_dict[s])

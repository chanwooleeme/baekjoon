import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(n):
        for j in range(i):
            
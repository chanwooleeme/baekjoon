import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * len(arr)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            dp[i]
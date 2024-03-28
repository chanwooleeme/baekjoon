import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    dp = [50000 for _ in range(5001)]
    dp[3] = 1
    dp[5] = 1
    for i in range(5, 5001):
        dp[i] = min([dp[i], dp[i-3]+1, dp[i-5]+1])
    if dp[N] == 50000:
        print(-1)
    else:
        print(dp[N])
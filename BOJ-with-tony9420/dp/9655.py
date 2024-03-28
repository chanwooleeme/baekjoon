import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    INF = 1001
    dp = [0 for _ in range(INF)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    for i in range(4, INF):
        dp[i] = min(dp[i-1]+1, dp[i-3]+1)
    if dp[N] % 2 == 1:
        print('SK')
    else:
        print('CY')

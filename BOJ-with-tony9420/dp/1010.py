import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    INF = 31

    dp = [[0 for _ in range(INF)] for _ in range(INF)]
    for i in range(INF):
        dp[1][i] = i
    for i in range(2, INF):
        dp[i][i] = 1
        for j in range(i, INF):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    for _ in range(N):
        a, b = map(int, input().split())
        print(dp[a][b])
    
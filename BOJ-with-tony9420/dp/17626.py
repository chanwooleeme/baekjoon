import sys
import math

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    INF = N*N + 1
    dp = [0 for _ in range(INF)]
    dp[1] = 1
    for i in range(2, N+1):
        min_value = INF
        j = 1
        while (j ** 2) <= i:
            min_value = min(min_value, dp[i-(j**2)])
            j += 1
        dp[i] = min_value + 1
    print(dp[N])
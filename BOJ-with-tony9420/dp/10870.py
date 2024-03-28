import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    dp = [0 for _ in range(21)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, 21):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N])
    
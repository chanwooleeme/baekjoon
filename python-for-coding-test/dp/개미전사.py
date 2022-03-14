N = int(input())
data = list(map(int, input().split()))

dp = [data[0], data[1]] + [0] * (N - 2)
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + data[i])
print(dp[N-1])

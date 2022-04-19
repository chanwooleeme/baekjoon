N = int(input())
arr = []
dp = [0 for _ in range(N)]
for _ in range(N):
    arr.append(int(input()))
if N < 3:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    if N == 3:
        print(dp[2])
    else:
        for i in range(3, N):
            dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])
        print(dp[-1])
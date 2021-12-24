def dfs(n):
    global ans
    if n > N:
        return
    ans = max(ans, n)
    for i in data:
        n = n * 10 + i
        dfs(n)
        n = (n - i) // 10

N, K = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
dfs(0)
print(ans)
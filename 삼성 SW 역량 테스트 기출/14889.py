import sys

input = sys.stdin.readline

def dfs(num, cnt):
    global result
    if cnt == N //2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        result = min(result, abs(start - link))
    
    for i in range(num, N):
        if not visited[i]:
            visited[i] = True
            dfs(num + 1, cnt + 1)
            visited[i] = False
    

N = int(input())
result = 10e9
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N + 1)]
dfs(0, 0)
print(result)
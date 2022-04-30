import sys

input = sys.stdin.readline

def dfs(x, y, cnt, result):
    global ans
    if ans >= result + max_v * (3 - cnt):
        return
    if cnt == 3:
        ans = max(ans, result)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if not visited[nx][ny]:
            if cnt == 1:
                visited[nx][ny] = True
                dfs(x, y, cnt + 1, result + arr[nx][ny])
                visited[nx][ny] = False    
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, result + arr[nx][ny])
            visited[nx][ny] = False
    
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = max(map(max, arr))
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = False

print(ans)
        
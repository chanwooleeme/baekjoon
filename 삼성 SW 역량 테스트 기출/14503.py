import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = True

result = 1
while True:
    flag = False
    for _ in range(4):
        d = (d - 1) % 4
        nx, ny = r + dx[d], c + dy[d]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if arr[nx][ny]:
            continue
        if not visited[nx][ny]:
            result += 1
            visited[nx][ny] = True
            r, c = nx, ny
            flag = True
            break
    
    if not flag:
        if arr[r-dx[d]][c-dy[d]] == 1:
            print(result)
            break
        else:
            r, c = r-dx[d], c-dy[d]

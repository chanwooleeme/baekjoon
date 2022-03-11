import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for d in dxy:
            nx = d[0] + x
            ny = d[1] + y
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)
                
                            
sys.setrecursionlimit(10**6)
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    graph = []
    data = []
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        line = list(map(int, input().split()))
        for j in range(w):
            if line[j]:
                data.append((i, j))
        graph.append(line)
        
    cnt = 0
    for item in data:
        if not visited[item[0]][item[1]]:
            dfs(item[0], item[1])
            cnt += 1
    print(cnt)
    
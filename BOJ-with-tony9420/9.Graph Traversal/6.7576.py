import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

q = deque()
M, N = map(int, input().split())
visited = [[False] * M for _ in range(N)]
graph = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

while q:
    v = q.popleft()
    vx = v[0]
    vy = v[1]
    for d in range(4):
        x = dx[d] + vx
        y = dy[d] + vy
        if x < 0 or y < 0 or x >= N or y >= M:
            continue
        if graph[x][y] or graph[x][y] == -1:
            continue
        graph[x][y] = graph[vx][vy] + 1
        q.append([x, y])

result = -1
for g in graph:
    if 0 in g:
        print('-1')
        exit(0)
    result = max(max(g), result)
print(result - 1)
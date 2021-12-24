import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
visited = [[False] * N for _ in range(N)]
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input()))))

result = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(N):
    for j in range(N):
        if not graph[i][j]:
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True
        q = deque()
        q.append([i, j])
        cnt = 1
        while q:
            v = q.popleft()
            for d in range(4):
                cur_x = v[0] + dx[d]
                cur_y = v[1] + dy[d]
                if cur_x < 0 or cur_y < 0 or cur_x >= N or cur_y >= N:
                    continue
                if visited[cur_x][cur_y] or graph[cur_x][cur_y] == 0:
                    continue
                visited[cur_x][cur_y] = True
                q.append([cur_x, cur_y])
                cnt += 1
        result.append(cnt)
result.sort()
print(len(result))
for item in result:
    print(item)
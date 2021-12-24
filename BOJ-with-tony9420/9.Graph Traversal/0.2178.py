import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
d = [[0] * M for _ in range(N)] 
for _ in range(N):
    graph.append(list(map(int, list(input()))))

def bfs():
    q = deque()
    q.append([0, 0])
    while q:
        v = q.popleft()
        if not graph[v[0]][v[1]]:
            continue
        for i in range(4):
            cur_x = dx[i] + v[0]
            cur_y = dy[i] + v[1]
            
            if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >= M:
                continue
            if d[cur_x][cur_y]:
                continue
            q.append([cur_x, cur_y])
            d[cur_x][cur_y] = d[v[0]][v[1]] + 1

bfs()
print(d[N - 1][M - 1] + 1)
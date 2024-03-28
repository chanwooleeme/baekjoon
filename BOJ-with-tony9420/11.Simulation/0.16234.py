import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def open_country(i, j, visited):
    q = deque()
    q.append([i, j])
    
    visited[i][j] = True
    dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    idxs = [[i, j]]
    population = arr[i][j]
    n = 1
    
    flag = False
    
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                visited[nx][ny] = True
                idxs.append([nx, ny])
                q.append([nx, ny])
                population += arr[nx][ny]
                n += 1
                flag = True
                
    for idx in idxs:
        arr[idx[0]][idx[1]] = population // n
        
    return flag
    
N, L, R = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag += open_country(i, j, visited)
    if not flag:
        break
    result += 1
print(result)
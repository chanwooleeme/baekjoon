import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def validate(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def bfs(i, j):
    q = deque()
    distance = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited[i][j] = False
    q.append((i, j))
    country_list = [(i, j)]
    population = arr[i][j]
    country = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for d in distance:
            nx = d[0] + x
            ny = d[1] + y
            if validate(nx, ny):
                diff = abs(arr[x][y] - arr[nx][ny])
                if not visited[nx][ny] and L <= diff <= R:
                    visited[nx][ny] = True
                    country_list.append((nx, ny))
                    population += arr[nx][ny]
                    country += 1
                    q.append((nx, ny))
                    
    if country > 1:
        for item in country_list:
            x, y = item
            arr[x][y] = population // country
            print(arr[x][y])
        return True
    return False
        
#입력
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if bfs(i, j):
                cnt += 1

print(cnt)
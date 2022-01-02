import sys
import copy
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def get_pos():
    virus, empty = [], []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                empty.append((i, j))
            elif arr[i][j] == 2:
                virus.append((i, j))
    return virus, empty

def set_wall(comb):
    for x, y in comb:
        arr[x][y] = 1
    
def collapse_wall(comb):
    for x, y in comb:
        arr[x][y] = 0

def bfs(virus):
    q = deque(virus)
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    tmp_arr = copy.deepcopy(arr)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()
        cnt += 1
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and tmp_arr[nx][ny] == 0:
                    tmp_arr[nx][ny] = 2
                    q.append((nx, ny))
    return cnt
        
#입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus, empty = get_pos()
combs = combinations(empty, 3)
result = -1
for comb in combs:
    set_wall(comb)
    virus_cnt = bfs(virus)
    wall_cnt = m * n - len(virus) - len(empty) + 3
    result = max(result, m * n - virus_cnt - wall_cnt)
    collapse_wall(comb)
print(result)
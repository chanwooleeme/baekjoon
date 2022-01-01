import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def get_pos():
	empty = []
	virus = []
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 0:
				empty.append((i, j))
			elif arr[i][j] == 2:
				virus.append((i, j))
	return empty, virus

def set_wall(comb):
	for x, y in comb:
		arr[x][y] = 1

def collapse_wall(comb):
	for x, y in comb:
		arr[x][y] = 0
				
def bfs(virus):
    q = deque(virus)
    visited = [[False] * m for _ in range(n)]
    count = len(virus)
    while q:
        q_size = len(q)
        for _ in range(q_size):
            x, y = q.popleft()
            visited[x][y] = True
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y
                if (0 <= nx < n) and (0 <= ny < m):
                    if arr[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        count += 1
    return count

#입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

empty, virus = get_pos()
combs = combinations(empty, 3)

count = int(1e9)

for comb in combs:
	set_wall(comb)
	
	temp = bfs(virus)
	if temp < count:
		count = temp
	collapse_wall(comb)

wall = n * m - (len(empty)  + len(virus))
print(n * m - (count + wall + 3))
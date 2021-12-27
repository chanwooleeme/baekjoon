import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
M, N = map(int, input().split())
board = []
visited = [[False] * M for _ in range(N)]
odd_dx = [-1, -1, 0, 1, 1, 0]
odd_dy = [0, -1, -1, -1, 0, 1]
even_dx = [-1, -1, 0, 1, 1, 0]
even_dy = [0, 1, 1, 1, 0, -1]
in_q = deque()
q = deque()

for _ in range(N):
    board.append(list(map(int, input().split())))

def valid(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    return True

def outer(_x, _y, dx, dy):
    cnt = 0
    for i in range(6):
        x = _x + dx[i]
        y = _y + dy[i]
        if not valid(x, y):
            continue
        if board[x][y] == 1 or board[x][y] == -1:
            cnt += 1
    return 6 - cnt


def dfs(x, y):
    if x % 2 == 0:
        for i in range(6):
            nx = x + odd_dx[i]
            ny = y + odd_dy[i]
            if not visited[nx][ny] and not board[nx][ny] and valid(X,y):
                dfs(nx, ny)
            else:
                return
    elif x % 2 == 1:
        for i in range(6):
            nx = x + even_dx[i]
            ny = y + even_dy[i]
            if not visited[nx][ny] and not board[nx][ny] and valid(x,y):
                dfs(nx, ny)        
            else:
                return
    return 1
def bfs_init():
    tmp = []
    while in_q:
        _x, _y = in_q.popleft()
        visited[_x][_y] = True
        if _x % 2:
            for i in range(6):
                x = _x + odd_dx[i]
                y = _y + odd_dy[i]
                if not valid(x, y):
                    return
                if board[x][y] or visited[x][y]:
                    continue
                in_q.append((x, y))
        else:
            for i in range(6):
                x = _x + even_dx[i]
                y = _y + even_dy[i]
                if not valid(x, y):
                    return
                if board[x][y] or visited[x][y]:
                    continue
                tmp.append((x, y))
    print(tmp)
    for item in tmp:
        x, y = item
        board[x][y] = -1

def bfs():
    result = 0
    while q:
        _x, _y = q.popleft()
        if _x % 2:
            result += outer(_x, _y, odd_dx, odd_dy)
        else:
            result += outer(_x, _y, even_dx, even_dy)
    return result

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            in_q.append((i, j))
        elif board[i][j] == 1:
            q.append((i, j))
bfs_init()
for g in board:
    print(*g)
print(bfs())
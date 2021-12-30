import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def valid(x, y):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    return True

q = deque()
w, h = map(int, input().split())
board = [[0] * w]
for _ in range(h):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0] * w)
odd_dx = [-1, -1, 0, 1, 1, 0]
odd_dy = [0, -1, -1, -1, 0, 1]
even_dx = [-1, -1, 0, 1, 1, 0]
even_dy = [0, 1, 1, 1, 0, -1]

for i in range(h):
    for j in range(w):
        if not board[i][j]:
            q.append((i, j))
result = 0
while not q:
    x, y = q.popleft()
    cnt = 0
    if x % 2 == 0:
        for i in range(6):
            nx = x + even_dx[i]
            ny = y + even_dy[i]
            if not valid(nx, ny):
                continue
            if board[nx][ny]:
                cnt += 1
    else:
        for i in range(6):
            nx = x + even_dx[i]
            ny = y + even_dy[i]
            if not valid(nx, ny):
                continue
            if board[nx][ny]:
                cnt += 1
    if cnt != 6:
        result += cnt
print(result)
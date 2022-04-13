import sys

sys.setrecursionlimit(10 ** 6)

def input():
    return sys.stdin.readline().rstrip()

def dfs(x, y):
    if dp_board[x][y]:
        return dp_board[x][y]
    dp_board[x][y] = 1
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] > board[x][y]:
            dp_board[x][y] = max(dp_board[x][y], dfs(nx, ny) + 1)
    return dp_board[x][y]

n = int(input())
board = []
dp_board = [[0] * n for _ in range(n)]
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if dp_board[i][j] == 0:
            dfs(i, j)
    
max_val = 0        
for item in dp_board:
    max_val = max(max_val, max(item))
print(max_val)
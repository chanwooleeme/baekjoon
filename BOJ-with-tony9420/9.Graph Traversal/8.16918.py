import sys
from collections import deque

def input():
	return sys.stdin.readline().rstrip()

R, C, N = map(int, input().split())
N -= 1
board = []
for _ in range(R):
	board.append(list(input()))
 
def bfs(bomb):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while bomb:
        nx, ny = bomb.popleft()
        board[nx][ny] = '.'
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or y < 0 or x >= R or y >= C:
                continue
            board[x][y] = '.'
            
while N:
    bomb = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb.append((i, j))
            else:
                board[i][j] = 'O'
    N -= 1
    if N == 0:
        break
    bfs(bomb)
    N -= 1
    
for item in board:
    print(''.join(item))
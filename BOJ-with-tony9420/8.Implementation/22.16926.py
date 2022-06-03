import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def rotate(x, y, height, width, R):
    global board
    q = deque()
    
    for i in range(width - 1): #top left
        q.append(board[x][y+i])
    for i in range(height - 1): # top right
        q.append(board[x+i][y + width - 1])
    for i in range(width - 1):
        q.append(board[x + height - 1][y + width - 1 - i])
    for i in range(height - 1):
        q.append(board[x + height -1 -i][y])
        
    q.rotate(-R)
    
    for i in range(width - 1): #top left
        board[x][y+i] = q.popleft()
    for i in range(height - 1): # top right
        board[x+i][y + width - 1] = q.popleft()
    for i in range(width - 1):
        board[x + height - 1][y + width - 1 - i] = q.popleft()
    for i in range(height - 1):
        board[x + height -1 -i][y] = q.popleft()   
    
N, M, R = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

n, m = N, M
x, y = 0, 0

for _ in range(min(N, M) // 2):
    rotate(x, y, n, m, R)
    x, y = x+1, y+1
    n, m = n - 2, m - 2

for item in board:
    for num in item:
        print(num, end=' ')
    print()
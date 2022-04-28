import sys
from collections import deque

input = sys.stdin.readline

def dummy():
    x, y = 0, 0
    end_x, end_y = 0,0
    time = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    snake = deque()
    snake.append([0, 0])
    while True:
        time += 1
        
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        if [nx, ny] in snake:
            break
        if arr[nx][ny] == 0:
            snake.popleft()
        arr[nx][ny] = 0
        snake.append([nx, ny])
        x, y = nx, ny
        
        if directions:
            if time == directions[0][0]:
                direction = directions.popleft()
                if direction[1] == 'D':
                    d = (d + 1) % 4
                else:
                    d = (d - 1) % 4
                
    print(time)

N = int(input())
K = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
    
directions = deque()
L = int(input())
for _ in range(L):
    X, C = input().split()
    X = int(X)
    directions.append([X, C])

dummy()
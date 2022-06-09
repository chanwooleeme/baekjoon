import sys

def input():
    return sys.stdin.readline().rstrip()

def check_board(start, x, y):
    global N, M
    
    _x, _y = x%2, y%2
    cnt = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if i % 2 == _x: #짝수줄
                if j % 2 == _y and board[i][j] != start:
                    cnt += 1
                elif j % 2 != _y and board[i][j] == start:
                    cnt += 1
            else:
                if j % 2 == _y and board[i][j] == start:
                    cnt += 1
                elif j % 2 != _y and board[i][j] != start:
                    cnt += 1
    return cnt

N, M = map(int, input().split())
board = list(list(input()) for _ in range(N))

result = 10e9

for i in range(0, N - 7):
    for j in range(0, M - 7):
        result = min(result, min(check_board('W', i, j), check_board('B', i, j)))
        
print(result)
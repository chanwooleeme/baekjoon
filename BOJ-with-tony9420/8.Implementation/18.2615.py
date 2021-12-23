def range_validate(x, y):
    if x < 0 or x > 18 or y < 0 or y > 18:
        return False
    return True

def count(board, x, y, dx, dy, val):
    cnt = 1
    x1 = x
    y1 = y
    for _ in range(18):
        x += dx
        y += dy
        if range_validate(x, y):
            if val == board[x][y]:
                cnt += 1
            else:
                break
        else:
            break
    if cnt == 5:
            return True
    return False

def validate(board, x, y, dx, dy):
    if not range_validate(x-dx, y-dy):
        return True
    else:
        if board[x][y] != board[x-dx][y-dy]:
            return True
    return False

board = []

for _ in range(19):
    board.append(list(map(int, input().split())))
    
dx = [0, 1, 1, -1, -1]
dy = [1, 1, 0, 1, 0]

for j in range(19):
    for i in range(19):
        if not board[i][j]:
            continue
        for d in range(5):
            if count(board, i, j, dx[d], dy[d], board[i][j]):
               if validate(board, i, j, dx[d], dy[d]):
                   print(board[i][j])
                   print(i+1, j+1)
                   exit(0)
print(0)
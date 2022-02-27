board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
dxy = [[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

visited = []
result = []
for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        item = board[i][j]
        for d in dxy:
            cnt = 0
            dx = d[0]
            dy = d[1]
            tmp = []
            v = [[i, j]]
            if v in visited:
                break
            for k in range(6):
                x = i + (dx * k)
                y = j + (dy * k)
                if x < 0 or y < 0 or x >= 19 or y >= 19 or board[x][y] != item:
                    break
                cnt += 1
                tmp.append([x, y])
            if cnt == 5:
                valid = 0
                for t in tmp:
                    if t in visited:
                        valid += 1
                if valid != 5:
                    x1 = tmp[0][0]
                    y1 = tmp[0][1]
                    x2 = tmp[-1][0]
                    y2 = tmp[-1][1]
                    if y1 < y2:
                        result.append([item, x1, y1])
                    elif y1 > y2:
                        result.append([item, x2, y2])
                    else:
                        if x1 < x2:
                            result.append([item, x1, y1])
                        else:
                            result.append([item, x2, y2])
            elif cnt > 5:
                for t in tmp:
                    visited.append(t)
if not result:
    print(0)
else:
    print(result[0][0])
    print(result[0][1] + 1, result[0][2] + 1)



N = int(input())

def first_rule(student):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    li = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count = 0
                blank = 0
                for d in dxy:
                    x = i + d[0]
                    y = j + d[1]
                    if x < 0 or x >= N or y < 0 or y >= N:
                        continue
                    if board[x][y] in like[student]:
                        count += 1
                    elif board[x][y] == 0:
                        blank += 1
                li.append([count, blank, i, j])
    
    max_item = max(li, key = lambda x:x[0])[0]
    max_li = []
    for item in li:
        if item[0] == max_item:
            max_li.append(item[1:])
    return max_li

def second_rule(data):
    blank_li = []
    max_blank_item = max(data, key = lambda x:x[0])[0]
    for item in data:
        if item[0] == max_blank_item:
            blank_li.append(item[1:])

    return blank_li

def third_rule(data):
    row_li = []
    min_row = min(data, key = lambda x:x[0])[0]
    for item in data:
        if item[0] == min_row:
            row_li.append(item)
    return min(row_li, key = lambda x:x[1])

like = [[0] * 4 for _ in range(N * N + 1)]
board = [[0] * N for _ in range(N)]
orders = []

for _ in range(N * N):
    inputs = list(map(int, input().split()))
    like[inputs[0]] = inputs[1:]
    orders.append(inputs[0])

board[1][1] = orders[0]

for order in orders[1:]:
    student = order
    first_result = first_rule(student)
    if len(first_result) > 1:
        second_result = second_rule(first_result)
        if len(second_result) > 1:
            third_result = third_rule(second_result)
            result = third_result
        else:
            result = second_result[0]
    else:
        result = first_result[0][1:]
    board[result[0]][result[1]] = student

result = 0 
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(N):
        student = board[i][j]
        count = 0
        for d in dxy:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if board[x][y] in like[student]:
                count += 1     
        if count == 0 or count == 1:
            result += count
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        elif count == 4:
            result += 1000
print(result)
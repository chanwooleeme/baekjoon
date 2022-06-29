from collections import deque

def draw(rows, columns):
    idx = 1
    arr = []
    for _ in range(rows):
        tmp = []
        for j in range(columns):    
            tmp.append(idx)
            idx += 1
        arr.append(tmp)
    return arr

def rotate(board, query):
    q = deque()
    x1, y1, x2, y2 = map(lambda x : x-1, query)
    for i in range(y1, y2):
        q.append(board[x1][i])
    for i in range(x1, x2):
        q.append(board[i][y2])
    for i in range(y2, y1, -1):
        q.append(board[x2][i])
    for i in range(x2, x1, -1):
        q.append(board[i][y1])
    
    min_value = min(q)
    q.rotate(1)
    for i in range(y1, y2):
        board[x1][i] = q.popleft()
    for i in range(x1, x2):
        board[i][y2] = q.popleft()
    for i in range(y2, y1, -1):
        board[x2][i] = q.popleft()
    for i in range(x2, x1, -1):
        board[i][y1] = q.popleft()

    return min_value

def solution(rows, columns, queries):
    answer = []
    board = draw(rows, columns)
    for query in queries:
        answer.append(rotate(board, query))
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
from collections import deque

def bfs(maps):
    q = deque()
    r = len(maps)
    c = len(maps[0])
    graph = [[-1] * c for _ in range(r)]
    
    q.append([0, 0])
    graph[0][0] = 1
    
    dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    while q:
        cur_x, cur_y = q.popleft()
        for d in dxy:
            nx = cur_x + d[0]
            ny = cur_y + d[1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if maps[nx][ny] == 0 or graph[nx][ny] != -1:
                continue
            graph[nx][ny] = graph[cur_x][cur_y] + 1
            q.append([nx,ny])
    return graph[-1][-1]

def solution(maps):
    return bfs(maps)

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	)
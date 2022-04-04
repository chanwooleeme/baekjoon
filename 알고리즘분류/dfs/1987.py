import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(x, y, t):
    global result
    result = max(result, t)
    
    for d in dxy:
        nx = d[0] + x
        ny = d[1] + y
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if not visited[board[nx][ny]]:
            visited[board[nx][ny]] = True
            dfs(nx, ny, t + 1)
            visited[board[nx][ny]] = False
    
sys.setrecursionlimit(10**6)
R, C = map(int, input().split())

board = []
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(R):
    l = list(input())
    tmp = []
    for item in l:
        tmp.append(ord(item) - 65)
    board.append(tmp)

result = 0
visited = [False] * 26
visited[board[0][0]] = True
dfs(0, 0, 1)
print(result)
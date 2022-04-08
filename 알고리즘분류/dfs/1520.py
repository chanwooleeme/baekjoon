import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def dfs(x, y):
    if x == N-1 and y == M - 1:
        return 1
    elif dp[x][y] == -1:
        dp[x][y] = 0
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]
    
N, M = map(int, input().split())
board = []
dp = [[-1] * M for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(N):
    board.append(list(map(int, input().split())))

print(dfs(0, 0))
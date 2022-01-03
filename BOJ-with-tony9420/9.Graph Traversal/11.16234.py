import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def validate(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def bfs():
    distance = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    q = deque((0, 0))
    change_idx = []
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for d in distance:
                        nx = d[0] + x
                        ny = d[1] + y
                        if validate(nx, ny):
                            diff = abs(arr[x][y] - arr[nx][ny])
                            if not visited[nx][ny] and L <= diff <= R:
                                visited[nx][ny] = True
                                flag = True
    return False

#입력
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
while bfs():
    cnt += 1
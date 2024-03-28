import sys

def input():
    return sys.stdin.readline().rstrip()

def rain_flower_magic():
    return

def copy_water_magic(x, y):
    for d in [dxy[2], dxy[4], dxy[6], dxy[8]]:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if arr[nx][ny]:
            arr[x][y] += 1

N, M = map(int, input().split())
arr = []
order = []
dxy = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
goorm = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(M):
    vector, iter = map(int, input().split())
    visited = [[False] * N for _ in range(N)]
    
    d = [0, 0]
    d[0] = dxy[vector][0] * iter
    d[1] = dxy[vector][1] * iter
    
    for i in range(len(goorm)):
        goorm[i][0] = (goorm[i][0] + d[0]) % N
        goorm[i][1] = (goorm[i][1] + d[1]) % N
        visited[goorm[i][0]][goorm[i][1]] = True
        arr[goorm[i][0]][goorm[i][1]] += 1
    
    while goorm:
        x, y = goorm.pop()  
        copy_water_magic(x, y)
        
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                visited[i][j] = True
                goorm.append([i, j])
                arr[i][j] -= 2
    
result = 0 
for item in arr:
    result += sum(item)
print(result)
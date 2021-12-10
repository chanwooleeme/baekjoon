import sys

def input():
    return sys.stdin.readline().rstrip()

def isfind(cnt, x, y):
    if cnt == find:
        find_xy[0] = x+1
        find_xy[1] = y+1

N = int(input())
find = int(input())
mid = N//2
find_xy = [mid+1, mid+1]
cnt = 1

field = [[0]*N for _ in range(N)]
field[mid][mid] = 1
x = mid
y = mid
step = 3
while step <= N:
    cnt += 1 #위
    x = x - 1
    field[x][y] = cnt
    isfind(cnt, x, y)
    
    for _ in range(step - 2):
        y = y + 1
        cnt += 1
        field[x][y] = cnt
        isfind(cnt, x, y)
    
    for _ in range(step - 1):
        x = x + 1
        cnt += 1
        field[x][y] = cnt
        isfind(cnt, x, y)
        
    for _ in range(step - 1):
        y = y - 1
        cnt += 1
        field[x][y] = cnt
        isfind(cnt, x, y)
        
    for _ in range(step - 1):
        x = x - 1
        cnt += 1
        field[x][y] = cnt
        isfind(cnt, x, y)
    step += 2
    
for i in range(N):
    result = []
    for j in range(N):
        result.append(str(field[i][j]))
    print(" ".join(result))
print(find_xy[0], find_xy[1])
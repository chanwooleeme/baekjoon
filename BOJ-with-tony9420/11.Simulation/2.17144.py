import sys

def input():
    return sys.stdin.readline().rstrip()

def spread_dust(dusts):
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    batch_li = []
    for dust in dusts:
        x = dust[0]
        y = dust[1]
        dust_amount = arr[x][y] // 5
        cnt = 0
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if arr[nx][ny] == -1:
                continue
            cnt += 1
            batch_li.append([nx, ny, dust_amount])
        arr[x][y] -= (dust_amount * cnt)
    
    for item in batch_li:
        x = item[0]
        y = item[1]
        v = item[2]
        arr[x][y] += v
        
def start_air_cleaner(air_cleaner):
    d_top = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    d_bottom = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    top_x = air_cleaner[0][0] + d_top[0][0]
    top_y = air_cleaner[0][1] + d_top[0][1]
    bottom_x = air_cleaner[1][0] + d_bottom[0][0]
    bottom_y = air_cleaner[1][1] + d_bottom[0][1]
    
    i, tmp = 0, 0
    while i < 4:
        tmp2 = arr[top_x][top_y]
        arr[top_x][top_y] = tmp
        top_x += d_top[i][0]
        top_y += d_top[i][1]
        tmp = tmp2
        if (top_x == air_cleaner[0][0] and top_y == C-1) \
            or (top_x == 0 and top_y == C-1) \
                or (top_x == 0 and top_y == 0) \
                    or (top_x == air_cleaner[0][0] and top_y ==0):
            i += 1    
    
    i, tmp = 0, 0
    while i < 4:
        tmp2 = arr[bottom_x][bottom_y]
        arr[bottom_x][bottom_y] = tmp
        bottom_x += d_bottom[i][0]
        bottom_y += d_bottom[i][1]
        tmp = tmp2
        if (bottom_x == air_cleaner[1][0] and bottom_y == C-1) \
            or (bottom_x == R-1 and bottom_y == C-1) \
                or (bottom_x == R-1 and bottom_y == 0) \
                    or (bottom_x == air_cleaner[1][0] and bottom_y ==0):
            i += 1
    
R, C, T = map(int, input().split())
arr = []
air_cleaner = []
for _ in range(R):
    arr.append(list(map(int, input().split())))

for _ in range(T):
    dusts = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                air_cleaner.append([i, j])
            elif arr[i][j] != 0:
                dusts.append([i, j])
    spread_dust(dusts)
    start_air_cleaner(air_cleaner)
    
result = 0
for item in arr:
    result += sum(item)
print(result + 2)
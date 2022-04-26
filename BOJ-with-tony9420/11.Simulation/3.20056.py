import sys
    
def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
arr = [[] for _ in range(N)]
dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for item in arr:
    for _ in range(N):
        item.append([])
        
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, d, s])

while K > 0:
    tmps = []
    idxs = []
    for i in range(N):
        for j in range(N):
            while arr[i][j]:
                m, d, s = arr[i][j].pop()
                x = (i + (dxy[d][0] * s)) % N
                y = (j + (dxy[d][1] * s)) % N
                tmps.append([x, y, m, d, s])

    for tmp in tmps:
        x, y, m, d, s = tmp
        arr[x][y].append([m, d, s])
    
    for i in range(N):
        for j in range(N):
            l = len(arr[i][j])
            if l > 1:
                m, s = 0, 0
                is_even = False
                is_odd = False
                d = []
                while arr[i][j]:
                    _m, _d, _s = arr[i][j].pop()
                    m += _m
                    s += _s
                    if _d % 2:
                        is_odd = True
                    else:
                        is_even = True
                m //= 5
                if m == 0:
                    continue
                s //= l
                if not is_even * is_odd:
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                for _d in range(4):
                    arr[i][j].append([m, d[_d], s])

    K -=1
    
result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for data in arr[i][j]:
                result += data[0]    
print(result)
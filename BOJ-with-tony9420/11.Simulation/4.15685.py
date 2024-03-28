max_int = 101
dragon = []
d_x = [0, -1, 0, 1]
d_y = [1, 0, -1, 0]
end_x = 0
end_y = 0

N = int(input())
arr = [[False for col in range(max_int)] for row in range(max_int)]

def make_generation():
    size = len(dragon)
    for i in range(size - 1, -1, -1):
        dir = (dragon[i] + 1) % 4
        
        global end_x, end_y
        end_x += d_x[dir]
        end_y += d_y[dir]
        
        arr[end_x][end_y] = True
        
        dragon.append(dir)
    
    
    
for _ in range(N):
    y, x, d, g = map(int, input().split())
    
    dragon.clear()
    
    arr[x][y] = True
    
    end_x = x + d_x[d]
    end_y = y + d_y[d]
    arr[end_x][end_y] = True
    
    dragon.append(d)
    
    for i in range(g):
        make_generation()

result = 0
for i in range(max_int - 1):
    for j in range(max_int - 1):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            result += 1
            
print(result)

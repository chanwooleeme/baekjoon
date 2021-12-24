N, M = map(int, input().split())
data = [[False] * 201 for _ in range(201)]
for _ in range(M):
    key, val = map(int, input().split())
    data[key][val] = True
    data[val][key] = True
    data.append([key, val])
    
result = 0 
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if data[i][j] or data[i][k] or data[j][k]:
                continue
            result += 1
print(result)
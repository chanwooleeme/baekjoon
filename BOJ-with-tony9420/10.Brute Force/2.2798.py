N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
max_comb = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(i + 2, N):
            tmp = data[i] + data[j] + data[k]
            if tmp <= M:
            	max_comb = max(max_comb, tmp)
print(max_comb)
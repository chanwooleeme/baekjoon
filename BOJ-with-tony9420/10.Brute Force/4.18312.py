N, K = map(int, input().split())
cnt = 0
K = str(K)
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            s_i = str(i)
            if i < 10:
                s_i += '0'
            s_j = str(j)
            if j < 10:
                s_j += '0'
            s_k = str(k)
            if k < 10:
                s_k += '0'
            if K in s_i or K in s_j or K in s_k:
                cnt += 1
print(cnt)
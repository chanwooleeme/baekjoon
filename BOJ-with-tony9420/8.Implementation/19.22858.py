N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))
P = [0] * (N + 1)

for _ in range(K):
    for i in range(1, N + 1):
        P[D[i]] = S[i]
    S[:] = P[:]
print(*P[1:])
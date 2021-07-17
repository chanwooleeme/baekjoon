H, M = map(int, input().split())

M = H * 60 + M - 45
print(M // 60, M % 60)

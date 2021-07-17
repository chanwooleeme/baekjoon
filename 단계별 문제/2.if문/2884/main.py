H, M = map(int, input().split())

X = H * 60 + M - 45
print(X // 60 % 24, X % 60)

n = int(input())
li = [0, 1, 2] + [0] * (n-1)
for i in range(3, n+1):
    li[i] = li[i-1] + li[i-2]
print(li[n] % 10007)
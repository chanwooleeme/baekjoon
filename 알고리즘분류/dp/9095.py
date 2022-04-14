T = int(input())
for _ in range(T):
    n = int(input())
    li = [0] * (n+1)
    li[1] = 1
    li[2] = 2
    li[3] = 4
    if n < 4:
        print(li[n])
    else:
        for i in range(4, n+1):
            li[i] = li[i-1] + li[i-2] + li[i-3]
        print(li[n])
    
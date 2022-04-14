T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        li = [[0, 0] for _ in range(n + 1)]
        li[0] = [1, 0]
        li[1] = [0, 1]
        for i in range(2, n+1):
            li[i][0] = li[i-2][0] + li[i-1][0]
            li[i][1] = li[i-2][1] + li[i-1][1]
        print(li[n][0], li[n][1])
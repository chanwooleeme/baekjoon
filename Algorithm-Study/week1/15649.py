N, M = map(int, input().split())
stack = []

def dfs(n):
    if n == M:
        for i in stack:
            print(i, end=' ')
        print()
        return
    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            dfs(n + 1)
            stack.pop()
dfs(0)
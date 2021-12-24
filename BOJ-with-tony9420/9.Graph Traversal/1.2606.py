N = int(input())
T = int(input())

visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(T):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)
    
def dfs(cur):
    global ans
    if not visited[cur]:
        visited[cur] = True
        ans += 1
        for node in graph[cur]:
            dfs(node)

ans = 0
dfs(1)
print(ans - 1)
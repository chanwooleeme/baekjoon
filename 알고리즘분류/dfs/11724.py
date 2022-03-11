import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(n):
    if not visited[n]:
        visited[n] = True
        for node in graph[n]:
            dfs(node)
            
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

cnt = 0
for i in range(1, N + 1):
    if not graph[i]:
        cnt += 1
    elif not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
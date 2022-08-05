from copy import deepcopy
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def dfs(n):
    dfs_visited[n] = True
    for node in dfs_graph[n]:
        if not dfs_visited[node]:
            dfs_result.append(node)
            dfs(node)
    return

def bfs(n):
    q = deque()
    q.append(n)
    bfs_visited[n] = True
    while q:
        cur = q.popleft()
        bfs_result.append(cur)
        for node in bfs_graph[cur]:
            if not bfs_visited[node]:
                bfs_visited[node] = True
                q.append(node)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

for nodes in graph:
    if nodes:
        nodes.sort()
dfs_graph = deepcopy(graph)
dfs_visited = [False for _ in range(N + 1)]
dfs_result = [V]

bfs_graph = deepcopy(graph)
bfs_visited = [False for _ in range(N + 1)]
bfs_result = []

dfs(V)
bfs(V)

print(' '.join([str(x) for x in dfs_result]))
print(' '.join([str(x) for x in bfs_result]))
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def dfs(cur):
    if not visited_dfs[cur]:
        visited_dfs[cur] = True
        result_dfs.append(cur)
        for node in graph[cur]:
            dfs(node)
            
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if visited_bfs[cur]:
            continue
        result_bfs.append(cur)
        visited_bfs[cur] = True
        for node in graph[cur]:
            if not visited_bfs[node]:
                q.append(node)
            
N, M, V = map(int, input().split())

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
result_dfs = []
result_bfs = []
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)
    
for node in graph:
    node.sort()
    
dfs(V)
bfs(V)
print(*result_dfs)
print(*result_bfs)
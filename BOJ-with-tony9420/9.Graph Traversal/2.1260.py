import sys
from collections import deque
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

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
def dfs(cur):
    if not visited_dfs[cur]:
        visited_dfs[cur] = True
        result_dfs.append(cur)
        for node in graph[cur]:
            dfs(node)

def bfs(cur):
    q = deque()
    q.append(cur)
    while q:
        v = q.popleft()
        if visited_bfs[v]:
            continue
        result_bfs.append(v)
        visited_bfs[v] = True
        for node in graph[v]:
            if not visited_bfs[node]:
                q.append(node)

dfs(V)
print(*result_dfs)
bfs(V)
print(*result_bfs)
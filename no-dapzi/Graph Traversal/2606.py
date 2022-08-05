import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(n):
    visited[n] = True
    for node in graph[n]:
        if not visited[node]:
            dfs(node)
            
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]

for _ in range(int(input())):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)
    
dfs(1)

print(sum(visited) - 1)
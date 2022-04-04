import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(p, n):
    if p == p2:
        visited[p] = True
        global result
        result = n
        return
    if not visited[p]:
        visited[p] = True
        nodes = graph[p]
        for node in nodes:
            n += 1
            dfs(node, n)
            n -= 1

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
p1, p2 = map(int, input().split())
if p1 == p2:
    print(0)
    sys.exit(0)
m = int(input())
for _ in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)
result = -1
dfs(p1, 0)
print(result)
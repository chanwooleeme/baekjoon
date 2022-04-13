import sys

sys.setrecursionlimit(10 ** 6)

def input():
    return sys.stdin.readline().rstrip()

def dfs(n, d):
    for item in graph[n]:
        node, w = item[0], item[1]
        if distance[node] == -1:
            distance[node] = d + w
            dfs(node, d+w)
            
V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    li = list(map(int, input().split()))
    k = li[0]
    li = li[1:-1]
    for i in range(0, len(li), 2):
        v, l = li[i], li[i+1]
        graph[k].append([v, l])
        
distance = [-1] * (V+1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
distance = [-1] * (V+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))

import sys

sys.setrecursionlimit(10 ** 6)
def input():
    return sys.stdin.readline().rstrip()

def dfs(n, weight):
    for item in graph[n]:
        node, w = item[0], item[1]
        if distance[node] == -1:
            distance[node] = weight + w
            dfs(node, weight + w)

N = int(input())
graph = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)
distance[1] = 0
for _ in range(N - 1):
    k, v, l = map(int, input().split())
    graph[k].append((v, l))
    graph[v].append((k, l))
dfs(1, 0)
start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
dfs(start, 0)
print(max(distance))
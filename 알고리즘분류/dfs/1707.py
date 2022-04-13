import sys

sys.setrecursionlimit(10 ** 6)
def input():
    return sys.stdin.readline().rstrip()

def dfs(n, color):
    visited[n] = color
    nodes = graph[n]
    for node in nodes:
        if not visited[node]:
            if not dfs(node, -color):
                return False
        elif visited[node] == color:
            return False
    return True

K = int(input())

for _ in range(K):
    K, L = map(int, input().split())
    graph = [[] for _ in range(K + 1)]
    visited = [False] * (K + 1)
    for _ in range(L):
        k, v = map(int, input().split())
        graph[v].append(k)
        graph[k].append(v)
    
    for i in range(1, K+1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break
    print("YES" if result else "NO")
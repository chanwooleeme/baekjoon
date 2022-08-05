import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(n):
    q = deque()
    q.append(n)
    result[n] = 1
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if not result[node]:
                result[node] = cur
                q.append(node)
                
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

result = [0] * (N+1)
bfs(1)
for i in range(2, N+1):
    print(result[i])
import sys
from collections import deque
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(1, N):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

answer = []
def dfs(cur, parent):
    if not visited[cur]:
        visited[cur] = True
        answer.append([cur, parent])
        for node in graph[cur]:
                dfs(node, cur)
dfs(1, 1)
answer = answer[1:]
answer.sort()
for item in answer:
    print(item[1])
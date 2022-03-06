import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()
        
N = int(input())
graph = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = []

for _ in range(1, N):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

def dfs(cur, parent):
    if not visited[cur]:
        visited[cur] = True
        answer.append([cur, parent])
        for node in graph[cur]:
            dfs(node, cur)
dfs(1, 1)

answer = answer[2:]
answer.sort()
for item in answer:
    print(item[1])
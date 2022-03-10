from collections import deque

def bfs(n, graph, visited, distance):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if not visited[node]:
                distance[node] = distance[cur] + 1
                visited[node] = True
                q.append(node)
    max_val = max(distance)
    return distance.count(max_val)

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    for item in edge:
        k, v = item
        graph[k].append(v)
        graph[v].append(k)
    print(bfs(1, graph, visited, distance))
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

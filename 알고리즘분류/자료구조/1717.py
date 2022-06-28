import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [i for i in range(N + 1)]

def find(a):
    if graph[a] == a:
        return a
    tmp = find(graph[a])
    graph[a] = tmp
    return tmp
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        graph[b] = a
    else:
        graph[a] = b
for _ in range(M):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
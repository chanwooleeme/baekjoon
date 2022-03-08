import sys,heapq

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    max_q, min_q = [], []
    visited = [False] * 1_000_001
    for k in range(N):
        opr, n = input().split()
        n = int(n)
        if opr == 'I':
            visited[k] = True
            heapq.heappush(max_q, (-n, k))
            heapq.heappush(min_q, (n, k))
        else:
            if n == 1:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            elif n == -1:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    if max_q and min_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print("EMPTY")
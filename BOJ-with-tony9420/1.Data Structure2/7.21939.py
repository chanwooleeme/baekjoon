import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
visited = [False] * 110_001
max_q = []
min_q = []
k = 0
while k < N:
    P, L = map(int, input().split())
    heapq.heappush(max_q, (-L, P, k))
    heapq.heappush(min_q, (L, P, k))
    k += 1
M = int(input())
for _ in range(M):
    s = input().split()
    opr = s[0]
    if opr == 'add':
        heapq.heappush(max_q, (int(s[2]) * -1, int(s[1]), k))
        heapq.heappush(min_q, (int(s[2]), int(s[1]), k))
    else:
        L = int(s[1])
        if opr == 'recommend':
            if L == -1:
                while min_q and not visited[min_q[0][2]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][2]] = True
                    print(heapq.heappop(min_q))
            else:
                while max_q and not visited[max_q[0][2]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][2]] = True
                    print(-heapq.heappop(max_q))
    k += 1
import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)
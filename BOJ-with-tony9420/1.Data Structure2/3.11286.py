import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if heap:
        	print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [abs(a), a])
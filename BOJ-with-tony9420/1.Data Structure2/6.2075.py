import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

q = []
for _ in range(N):
    nums = list(map(int, input().split()))
    if not q:
        for num in nums:
            heapq.heappush(q, num)
    else:
        for num in nums:
            heapq.heappush(q, num)
            heapq.heappop(q)
print(heapq.heappop(q))
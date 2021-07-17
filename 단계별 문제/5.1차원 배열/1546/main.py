import sys

N = int(input())
li = list(map(int, sys.stdin.readline().split()))
M = max(li)
for i in range(N):
	li[i] = li[i] / M * 100
print(sum(li, 0.0) / len(li))

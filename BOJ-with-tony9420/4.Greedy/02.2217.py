import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = list()

for i in range(N): li.append(int(input().rstrip()))
li.sort(reverse=True)
if N == 1: print(li[0])
elif N == 2:
	print(li[1] * 2)
else:
	result = li[1] * 2
	for i in range(2, len(li)):
		result = max(result, li[i] * (i + 1))
	print(result)

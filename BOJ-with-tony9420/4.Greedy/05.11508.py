import sys

input = sys.stdin.readline
arr = []
n = int(input().rstrip())
for _ in range(n):
	arr.append(int(input().rstrip()))
arr.sort(reverse=True)
result = 0
for i in range(1, n + 1):
	if i % 3 != 0:
		result += arr[i - 1]
print(result)
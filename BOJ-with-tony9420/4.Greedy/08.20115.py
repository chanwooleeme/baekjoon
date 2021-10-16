n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = arr[0]
for i in range(1, n):
	result += arr[i] / 2
print(result)
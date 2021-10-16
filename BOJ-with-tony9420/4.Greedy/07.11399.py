n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr2 = list()
result = 0
for data in arr:
	result += data
	arr2.append(result)
print(sum(arr2))
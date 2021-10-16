n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if n % 2 == 0:
	max_val = 0
	arr1 = arr[:n // 2]
	arr2 = arr[n // 2:]
else:
	max_val = arr[n - 1]
	arr1 = arr[:(n - 1)//2]
	arr2 = arr[(n - 1)//2:]
arr1.sort(reverse=True)
result = arr1[0] + arr2[0]
for i in range(1, len(arr1)):
	result = max(result, arr1[i] + arr2[i])
result = max(result, max_val)
print(result)
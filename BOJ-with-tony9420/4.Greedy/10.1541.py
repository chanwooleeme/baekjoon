arr = input().split('-')
result = 0
for data in arr[0].split('+'):
	result += int(data)
for data in arr[1:]:
	for num in data.split('+'):
		result -= int(num)
print(result)
n = int(input())
numbers = map(int, input().split())
result = 0
for num in numbers :
	cnt = 1
	for i in range(1, num) :
		if num % i == 0 :
			cnt += 1
	if cnt == 2 :
		result += 1
print(result)
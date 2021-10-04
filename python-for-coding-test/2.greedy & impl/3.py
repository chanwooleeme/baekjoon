num = input()
result = int(num[0])
for i in range(1, len(num)) :
	n = int(num[i])
	if n <= 1 or result <= 1 :
		result += n
	else :
		result *= n
print(result)
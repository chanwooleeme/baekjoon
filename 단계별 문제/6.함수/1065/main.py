def hansu(num):
	result = 99
	for i in range(100, num + 1):
		string = list(map(int, str(i)))
		if string[0] - string[1] == string[1] - string[2]:
			result += 1
	return result

num = int(input())
if num < 100:
	print(num)
else:
	print(hansu(num))

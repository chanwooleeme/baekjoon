max = -1
idx = -1
for i in range(9):
	num = int(input())
	if max < num:
		max = num
		idx = i
print(max)
print(idx + 1)

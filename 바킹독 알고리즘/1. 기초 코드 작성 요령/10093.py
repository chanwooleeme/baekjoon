num1, num2 = map(int, input().split())
a = 0
b = 0
if num1 > num2 :
	a = num2
	b = num1
elif num1 < num2:
	a = num1
	b = num2
else :
	print(0)
	exit()
print(b - a - 1)
for i in range(a + 1, b) :
	if i != b-1 :
		print(i, end = ' ')
	else :
		print(i)
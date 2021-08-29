num = int(input())
div = 2
r = int(pow(num, 0.5))
while div <= r :
	while not num % div :
		print(div)
		num //= div
	div += 1

if num > 1 :
	print(num)
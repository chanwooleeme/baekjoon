t = int(input())
while t > 0 :
	x, y = map(int, input().split())
	n = y - x
	sqrt = int(pow(n, 0.5))
	if n == sqrt * sqrt :
		print(sqrt * 2 - 1)
	elif n > (sqrt * sqrt + sqrt) :
		print(sqrt * 2 + 1)
	else :
		print(sqrt * 2)
	t-=1

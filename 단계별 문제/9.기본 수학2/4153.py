while True :
	a, b, c = map(int, input().split())
	if not a and not b and not c :
		break
	li = [a, b, c]
	li.sort()
	if pow(li[0], 2) + pow(li[1], 2) == pow(li[-1], 2) :
		print("right")
	else :
		print("wrong")
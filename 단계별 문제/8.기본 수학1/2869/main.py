t = int(input())
while t > 0:
	h, w, n = map(int, input().split())
	if n % h == 0 :
		print(h * 100 + n//h)
	else :
		floor = n % h
		ho = n // h + 1
		print(floor * 100 + ho)
	t -= 1
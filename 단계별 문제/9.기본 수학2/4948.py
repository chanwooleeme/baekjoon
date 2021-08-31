limit = 123456
a = [False, False] + [True] * (limit * 2 - 1)
primes = [0, 0]
for i in range(2, limit * 2 + 1):
	if a[i] :
		primes.append(1)
		for j in range(2 * i, (limit * 2 + 1), i):
			a[j] = False
	else :
		primes.append(0)
while True:
	num = int(input())
	if not num :
		break
	print(sum(primes[num + 1 : num * 2 + 1]))
m = int(input())
n = int(input())
a = [False, False] + [True] * (n - 1)
# primes = []
results = []
for i in range(2, n + 1) :
	if a[i] :
		if i >= m :
			results.append(i)
		# primes.append(i)
		for j in range(2 * i, n + 1, i) :
			a[j] = False
if len(results) == 0 :
	print(-1)
else :
	print(sum(results))
	print(results[0])
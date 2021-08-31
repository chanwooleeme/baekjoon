n = int(input())
limit = 10000
a = [False, False] + [True] * (limit - 1)
for i in range(2, limit + 1) :
	if a[i] :
		for j in range(2 * i, limit + 1, i) :
			a[j] = False
while n > 0 :
	num = int(input())
	p_1 = p_2 = num // 2
	while not (a[p_1] and a[p_2]):
		p_1 -= 1
		p_2 += 1
	print(p_1, p_2)
	n -= 1
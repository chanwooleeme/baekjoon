t = int(input())
while t > 0 :
	k = int(input())
	n = int(input())
	li = [i for i in range(1, n + 1)]
	for i in range(1, k + 1) :
		for j in range(1, n) :
			li[j] += li[j - 1]
	print(li[-1])
	t-=1
n = int(input())

if n < 5:
	if n % 2 != 0:
		ans = -1
	else:
		ans = n // 2
else:
	ct, n = divmod(n, 5)
	if n == 0:
		ans = ct
	else:
		if n % 2 == 0:
			ct += n // 2
			ans = ct
		else:
			ct += (n + 5) // 2 - 1
			ans = ct
print(ans)
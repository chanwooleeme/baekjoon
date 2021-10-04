n, k = map(int, input().split())

result = 0
while n > 0 :
	tmp = (n // k) * k
	result += (n - tmp)
	n = tmp
	if n < k:
		break
	result += 1
	n //= k
result += (n - 1)
print(result)
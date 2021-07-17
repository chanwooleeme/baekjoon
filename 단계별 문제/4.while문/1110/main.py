N = int(input())
cnt = 0
tmp = N
while True:
	div = tmp // 10
	mod = tmp % 10
	new = div + mod
	new_div = new % 10
	cnt +=1
	result = mod * 10 + new_div
	if result == N:
		break
	tmp = result
print(cnt)
import math
n = int(input())
t = n // 3
result =  -1
while t >= 0 :
	tmp = n - (t * 3)
	if tmp % 5 == 0 :
		tmp_t = tmp // 5
		if result == -1 :
			result = t + tmp_t
		else :
			result = min(result, t + tmp_t)
	t -= 1
print(result)

n = int(input())
hour_without_3 = 15 * 60 + (45 * 15)
hour_with_3 = 60 * 60
result = 0
if n < 3 :
	result = hour_without_3 * n
elif n < 13:
	result = hour_without_3 * n + hour_with_3
elif n < 23:
	result = hour_without_3 * n + hour_with_3 * 2
else:
	result = hour_without_3 * n + hour_with_3 * 3
print(result)
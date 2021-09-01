li = list()
for i in range(9) :
	li.append(int(input()))
sum = sum(li)
for i in range(9) :
	for j in range(i + 1, 9) :
		num1 = li[i]
		num2 = li[j]
		if sum - num1 - num2 == 100 :
			li.remove(num1)
			li.remove(num2)
			li.sort()
			for k in range(7) :
				print(li[k])
			break
	if len(li) < 9 :
		break
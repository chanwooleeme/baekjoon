A = int(input())
B = int(input())
C = int(input())
li = list(str(A * B * C))
for i in range(10):
	print(li.count(str(i)))

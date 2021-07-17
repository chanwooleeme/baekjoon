import sys

C = int(input())

for i in range(C):
	a = list(map(int, sys.stdin.readline().split()))
	avg = sum(a[1:]) / a[0]
	count = 0
	for j in a[1:]:
		if j > avg:
			count += 1
	print(str("%.3f" %round((count / a[0] * 100), 3)) + "%")

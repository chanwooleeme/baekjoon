import sys

T = int(input())
for i in range(T):
	score = 0
	cnt = 0
	a = list(sys.stdin.readline())
	for j in range(len(a)):
		if a[j] == 'O':
			cnt += 1
			score += cnt
		else:
			cnt = 0
	print(score)

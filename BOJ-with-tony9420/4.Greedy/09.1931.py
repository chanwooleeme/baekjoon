import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = list()
for _ in range(n):
	s, e = map(int, input().split())
	li.append([s, e])
li.sort()
li.sort(key=lambda a:(a[1]))
cnt = 1
j = li[0][1]
for i in range(1, n):
	if li[i][0] >= j:
		cnt += 1
		j = li[i][1]
print(cnt)
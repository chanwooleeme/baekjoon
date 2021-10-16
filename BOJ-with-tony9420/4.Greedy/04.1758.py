import sys
input = sys.stdin.readline

n = int(input().rstrip())
li = list()
for i in range(n):
	li.append(int(input().rstrip()))
li.sort(reverse=True)

result = 0
for i in range(n):
	exp = li[i] - i
	if exp < 0:
		break
	result += exp
print(result)
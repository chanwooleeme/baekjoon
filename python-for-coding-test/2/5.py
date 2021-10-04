n = int(input())
data = list(input().split())
x, y = 1, 1
for i in data:
	if i == 'R' and y + 1 <= n:
		y += 1
	elif i == 'L' and y - 1 > 0:
		y -= 1
	elif i == 'U' and x - 1 > 0:
		x -= 1
	elif i == 'D' and x + 1 <= n:
		x += 1
print(x, y)
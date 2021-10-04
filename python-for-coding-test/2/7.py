data = input()
x = int(data[1])
y = ord(data[0]) - ord('a') + 1
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
count = 0

for i in range(len(dx)):
	new_x = x + dx[i]
	new_y = y + dy[i]
	if new_x < 1 or new_x > 8 or new_y < 1 or new_y > 8:
		continue
	else:
		count += 1
print(count)
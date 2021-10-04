data = input()
x = int(data[1])
y = ord(data[0]) - ord('a') + 1
# dx = [-2, -2, -1, 1, 2, 2, 1, -1]
# dy = [-1, 1, 2, 2, 1, -1, -2, -2]
steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
count = 0

for step in steps:
	new_x = x + step[0]
	new_y = y + step[1]
	if new_x >= 1 and new_x <= 8 and new_y >= 1 and new_y <= 8:
		count += 1
print(count)
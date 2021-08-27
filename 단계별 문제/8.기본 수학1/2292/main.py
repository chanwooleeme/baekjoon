N = int(input())
val = 1
add = 6
room_number = 1
if N == 1:
	print(1)
else :
	while True :
		val += add
		add += 6
		room_number += 1
		if N <= val :
			print(room_number)
			break
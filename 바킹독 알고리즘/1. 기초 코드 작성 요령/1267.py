n = int(input())
m = 0
y = 0
seconds = map(int, input().split())
for sec in seconds :
	y += (sec // 30 + 1) * 10
	m += (sec // 60 + 1) * 15
if m < y :
	print("M", m)
elif m > y:
	print("Y", y)
else :
	print("Y M", y)
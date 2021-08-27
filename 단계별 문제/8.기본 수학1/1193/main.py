N = int(input())
line = 1
while N > line :
	N -= line
	line += 1
if line % 2 == 0:
	a = N
	b = line + 1 - a
	print(a,'/',b, sep='')
else :
	b = N
	a = line + 1 - b
	print(a,'/',b, sep='')
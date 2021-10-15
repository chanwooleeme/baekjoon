import sys
input_str = input()
splited = input_str.split('.')
li = list()
for i in range(len(input_str)):
	if input_str[i] == '.':
		li.append(i)
s = str()
for data in splited:
	l = len(data)
	if l % 2 != 0:
		print(-1)
		sys.exit()
	else:
		four = l // 4
		two = l % 4 // 2
		s += "AAAA" * four + "BB" * two
for idx in li:
	s = s[:idx] + '.' + s[idx:]
print(s)
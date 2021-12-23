import sys

def input():
	return sys.stdin.readline().rstrip()

data = input()
result = ""
flag = False
tmp = ""
for char in data:
	if char == '<':
		flag = True
	elif char == '>':
		flag = False
	if flag:
		if tmp != "":
			result += tmp[::-1]
			tmp = ""
		result += char
	else:
		if char == '>':
			result += char
		else:
			if char == ' ':
				result += tmp[::-1]
				tmp = ""
				result += ' '
			else:
				tmp += char

result += tmp[::-1]
print(result)
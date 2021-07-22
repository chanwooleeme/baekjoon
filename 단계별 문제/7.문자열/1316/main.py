import sys

n = int(input())
li = list()
for i in range(n):
	li.append(sys.stdin.readline())
count = 0

for s in li:
	for i in range(len(s)):
		if i != len(s) - 1:
			if s[i] == s[i+1]:
				continue
			elif s[i] in s[i+1:]:
				break
		else:
			count+=1
print(count)

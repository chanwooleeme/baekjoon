import sys

li = list()
for i in range(10):
	n = int(sys.stdin.readline())
	li.append(n % 42)
li = set(li)
print(len(li))
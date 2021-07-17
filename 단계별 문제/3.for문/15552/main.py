import sys

inp = sys.stdin.readline()
T = int(inp)
for i in range(T):
	a, b = map(int, sys.stdin.readline().split())
	print(a + b)

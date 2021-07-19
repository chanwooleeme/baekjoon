inp = input()
li = [-1] * 26
for i in range(len(inp)):
	if li[ord(inp[i]) - ord("a")] == -1:
		li[ord(inp[i]) - ord("a")] = i
for i in li:
	print(i, end=" ")

li = sorted(list(map(int, input().split())))
if li[0] == li[1] == li[2] :
	print(li[0] * 1000 + 10000)
elif li[0] != li[1] and li[0] != li[2] and li[1] != li[2] :
	print(li[-1] * 100)
else :
	if li[0] == li[1] or li[0] == li[2]:
		print(li[0] * 100 + 1000)
	elif li[1] == li[2] :
		print(li[1] * 100 + 1000)

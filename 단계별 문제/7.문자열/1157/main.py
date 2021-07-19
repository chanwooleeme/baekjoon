s = input().upper()
li = list(set(s))

cnt = []
for i in li:
	cnt.append(s.count(i))
if cnt.count(max(cnt)) >= 2:
	print("?")
else:
	print(li[cnt.index(max(cnt))])

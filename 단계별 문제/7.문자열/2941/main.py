# s = input()
# li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# cnt = 0

# while len(s) > 0:
# 	flag = True
# 	for i in li:
# 		if s[0:len(i)] == i:
# 			s = s[len(i):]
# 			flag = False
# 			cnt += 1
# 	if flag:
# 		s = s[1:]
# 		cnt += 1
# print(cnt)
s = input()
m = len(s)
for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
	m -= s.count(i)
print(m)
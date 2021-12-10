import sys

def input():
    return sys.stdin.readline().rstrip()
                    
N = int(input())

bomb = list()
bomb_list = []
l = 0
for i in range(N):
    s = input()
    l = len(s)
    for j in range(len(s)):
        if s[j] == '*':
            bomb_list.append([i, j])
    bomb.append(list(s))

user = []

for _ in range(N):
    s = input()
    user.append(list(s))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
flag = False
for i in range(N):
    for j in range(l):
        if user[i][j] != 'x':
            continue
        if bomb[i][j] == '*':
            flag = True
        cnt = 0
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or x >= N or y < 0 or y >= l:
                continue
            if bomb[x][y] == '*':
                cnt += 1
        user[i][j] = str(cnt)
if flag:
    for item in bomb_list:
        x = item[0]
        y = item[1]
        user[x][y] = '*'

for i in range(N):
	result = []
	for j in range(N):
		result.append(user[i][j])
	print("".join(result)) 
import sys

def input():
    return sys.stdin.readline().rstrip()

def check_bingo():
    cnt = 0
    for i in range(5):
        if sum(is_bingo[i]) == 5:
           cnt += 1
    for i in range(5):
        sum_val = 0
        for j in range(5):
            sum_val += is_bingo[j][i]
        if sum_val == 5:
            cnt += 1
    cross_tmp1 = 0
    cross_tmp2 = 0
    for i in range(5):
        cross_tmp1 += is_bingo[i][i]
        cross_tmp2 += is_bingo[i][4-i]
    if cross_tmp1 == 5:
        cnt += 1
    if cross_tmp2 == 5:
        cnt += 1
    if cnt >= 3:
        return True
    else:
        return False
        
li = []
is_bingo = [[0]*5 for _ in range(5)]                        
li.append([0, 0, 0])
for i in range(5):
    tmp = list(map(int, input().split()))
    for j in range(5):
        li.append([tmp[j], i, j])
li.sort()
cnt = 1
for i in range(5):
    tmp = list(map(int, input().split()))
    for j in range(5): 
        x = li[tmp[j]][1]
        y = li[tmp[j]][2]
        is_bingo[x][y] = 1
        if check_bingo():
            print(cnt)
            exit(0)
        cnt += 1

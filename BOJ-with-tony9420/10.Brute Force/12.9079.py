from itertools import product
import copy
a = [0, 1]
prod = list(product(a, repeat=8))

T = int(input())
for _ in range(T):
    tmp_data = []
    answer = []
    for _ in range(3):
        strings = input().split()
        tmp = []
        for s in strings:
            if s == 'H':
                tmp.append(False)
            else:
                tmp.append(True)
        tmp_data.append(tmp)
    for p in prod:
        data = copy.deepcopy(tmp_data)
        if p[0]: #첫 가로줄
            data[0] = list(map(lambda x : not x, data[0]))
        if p[1]:
            data[1] = list(map(lambda x : not x, data[1]))
        if p[2]:
            data[2] = list(map(lambda x : not x, data[2]))
        if p[3]:
            for i in range(3):
                data[i][0] = not data[i][0]
        if p[4]:
            for i in range(3):
                data[i][1] = not data[i][1]
        if p[5]:
            for i in range(3):
                data[i][2] = not data[i][2]
        if p[6]:
            for i in range(3):
                data[i][i] = not data[i][i]
        if p[7]:
            for i in range(3):
                data[2-i][i] = not data[2-i][i]
        chk = 0
        for i in range(3):
            for j in range(3):
                chk += int(data[i][j])
        if chk == 0 or chk == 9:
            answer.append(sum(p))
    if answer:
        print(min(answer))
    else:
        print(-1)
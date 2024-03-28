import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(N)]
my_dict = dict()
for _ in range(M):
    oprs = list(map(int, input().split()))
    if len(oprs) > 2:
        n, i, x = oprs
        if n == 1:
            train[i-1][x-1] = 1
        else:
            train[i-1][x-1] = 0
    else:
        n, i = oprs
        if n == 3:
            tmp = [0] + train[i-1]
            tmp = tmp[:-1]
            train[i-1] = tmp
        else:
            tmp = train[i -1] + [0]
            tmp = tmp[1:]
            train[i-1] = tmp

cnt = 0                    
for item in train:
    s = ''.join(str(i) for i in item)
    if s in my_dict:
        continue
    else:
        my_dict[s] = True
        cnt += 1
        
print(cnt)
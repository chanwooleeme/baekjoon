def valid(s: str):
    for i in range(len(s)):
        if err[int(s[i])]:
            return False
    return True

def find():
    _min, _max = -1, -1
    for i in range(999999):
        s = str(i)
        if not valid(s):
            continue
        else:
            if i <= N:
                _min = i
            if i >= N:
                _max = i
                break
    return _min, _max

cur = 100

N = int(input())
M = int(input())
pad = [0, 1, 2, 3, 4, 5, 6 ,7 ,8, 9]
err = [False] * 10

if M != 0:
    for item in list(map(int, input().split())):
        err[item] = True
_min, _max = find()
if _min == -1 and _max != -1:
    result = min(abs(N - cur), len(str(_max)) + abs(N - _max))
elif _min != -1 and _max == -1:
    result = min(abs(N - cur), len(str(_min)) + abs(N - _min))
elif _min == -1 and _max == -1:
    result = abs(N - cur)
else:
    result = min(abs(N - cur), min(len(str(_min)) + abs(N - _min), len(str(_max)) + abs(N - _max)))
print(result)
def valid(n: int):
    s = str(n)
    if '666' in s:
        return True
    return False

N = int(input())

cnt = 0
i = 666
while True:
    if valid(i):
        cnt += 1
        if cnt == N:
            print(i)
            exit(0)
    i += 1
    
N = int(input())

def plus_all(n):
    s = str(n)
    cnt = n
    for item in s:
        cnt += int(item)
    return cnt

for i in range(N):
    if plus_all(i) == N:
        print(i)
        exit(0)
print(0)
import sys
    
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
calendar = [0] * 366

for _ in range(N):
    s, e = map(int, input().split())
    
    for i in range(s, e+1):
        calendar[i] += 1

result, width, height = 0, 0, 0
for i in range(len(calendar)):
    if calendar[i]:
        width += 1
        height = max(height, calendar[i])
    else:
        result += width * height
        width, height = 0, 0
result += width * height
print(result)
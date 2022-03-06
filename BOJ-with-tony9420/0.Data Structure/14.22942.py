import sys
    
def input():
    return sys.stdin.readline().rstrip()

def check(item, data):
    s1, e1 = item[0], item[1]
    s2, e2 = data[0], data[1]
    #내부이면
    if s1 < s2 and e1 > e2:
        return 1
    #외부이면
    elif e1 < s2 or e2 < s1:
        return 2
    else:
        return 0

N = int(input())
data = []
for _ in range(N):
    x, r = map(int, input().split())
    start, end = x - r, x + r 
    data.append([start, end])
data.sort()

recent = data[0]
stack = []
for i in range(1, N):
    tmp = check(recent, data[i])
    if tmp == 0:
            print("NO")
            exit(0)
    if stack:
        stack_tmp = check(stack[0], data[i])
        if stack_tmp == 0:
            print("NO")
            exit(0)
        elif stack_tmp == 2:
            stack.pop()
            break
    else:
        if tmp == 1:
            stack.append(recent)
    recent = data[i]
print("YES")
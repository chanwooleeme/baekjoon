import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    stack = []
    str = input()
    flag = False
    for i in range(len(str)):
        c = str[i]
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                flag = True
            else:
                stack.pop()
    if flag:
        print("NO")
    elif stack:
        print("NO")
    else:
        print("YES")
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

stack = []
for i in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]
    
    if cmd == "push":
        stack.append(X)
    elif cmd == "pop":
        if not stack:
            print("-1")
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
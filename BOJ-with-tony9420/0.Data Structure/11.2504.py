import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()
stack = []

for ch in s:
    if ch == ')' or ch == ']':
        if not stack:
            print(0)
            exit(0)
        if ch == ')' and stack[-1] == '(':
            stack.pop()
        elif ch == ']' and stack[-1] == '[':
            stack.pop()
        else:
            print(0)
            exit(0)
    else:
        stack.append(ch)
if stack:
    print(0)
    exit(0)

s = s.replace('()', '2').replace('[]', '3')
for ch in s:
    tmp = 0
    if ch == ')':
        while stack[-1] != '(':
            tmp += int(stack.pop())
        stack.pop()
        stack.append(str(tmp * 2))
    elif ch == ']':
        while stack[-1] != '[':
            tmp += int(stack.pop())
        stack.pop()
        stack.append(str(tmp * 3))
    else:
        stack.append(ch)
print(sum(list(map(int, stack))))
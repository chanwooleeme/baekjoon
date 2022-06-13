import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    stack = []
    s = input()
    if s == '.':
        break
    is_break = False
    for item in s:
        if item == '(':
            stack.append('(')
        elif item == '[':
            stack.append('[')
        elif item == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                is_break = True
                break
        elif item == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                is_break = True
                break
    if not is_break:
        if stack: print("no")
        else: print("yes")
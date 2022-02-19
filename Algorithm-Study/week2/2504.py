import sys

def input():
    return sys.stdin.readline().rstrip()

def print_zero_and_exit():
    print(0)
    exit(0)
    
def validate(s):
    stack = []
    for idx, c in enumerate(s):
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print_zero_and_exit()
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print_zero_and_exit()
    if stack:
        print_zero_and_exit()
    
s = input()
validate(s)
stack = []
result = 0
li = list(s.replace('()', '2').replace('[]', '3'))

for idx, item in enumerate(li):
    if item.isdigit():
        li[idx] = int(item)

for idx, item in enumerate(li):
    tmp = 0
    if item == '(' or item == '[' or type(item) == int:
        stack.append(item)
    elif item == ')':
        while True:
            top = stack.pop()
            if top == '(':
                break
            if top != ')':
                tmp += top
        stack.append(tmp * 2)
    elif item == ']':
        while True:
            top = stack.pop()
            if top == '[':
                break
            if top != ']':
                tmp += top
        stack.append(tmp * 3)
        
print(sum(stack))
import sys

def input():
    return sys.stdin.readline().rstrip()

S = input()
stack = list()
before = ''
result = 0
for item in S:
    if item == '(':
        stack.append(item)
    if item == ')':
        if before == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
    before = item
print(result)
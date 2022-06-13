import sys

def input():
    return sys.stdin.readline().rstrip()

l_stack = [input()]
r_stack = []
n = int(input())

for _ in range(n):
    oprs = list(input().split())
    if oprs[0] == 'P':
        l_stack.append(oprs[1])
        
    elif oprs[0] == 'L':
        if l_stack:
            r_stack.append(l_stack.pop())
            
    elif oprs[0] == 'D':
        if r_stack:
            l_stack.append(r_stack.pop())
            
    elif oprs[0] == 'B':
        if l_stack:
            l_stack.pop()
l_stack.extend(reversed(r_stack))
print(''.join(l_stack))
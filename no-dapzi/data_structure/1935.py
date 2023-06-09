import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
exp = list(input())
stack = []
result = 0

for i in range(N):
    num = input()
    for j in range(len(exp)):
        exp[j] = exp[j].replace(chr(65 + i), num)

for idx, val in enumerate(exp):
    if val.isdigit():
        stack.append(int(val))
    else:
        a = stack.pop()
        b = stack.pop()
        if val == '+':
            stack.append(b+a)
        elif val == '-':
            stack.append(b-a)
        elif val == '*':
            stack.append(b*a)
        elif val == '/':
            stack.append(b/a)

print(f"{stack.pop():.2f}")

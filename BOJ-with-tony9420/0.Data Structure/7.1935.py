import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
S = input()
S = list(S)

alpha = 65
for _ in range(N):
    c = input()
    for i, v in enumerate(S):
        if v == chr(alpha):
            S[i] = c
    alpha += 1
    
cal = []
for item in S:
    if item.isnumeric():
        cal.append(int(item))
    else:
        B = cal.pop()
        A = cal.pop()
        if item == '*':
            cal.append(A * B)
        elif item == '/':
            cal.append(A / B)
        elif item == '+':
            cal.append(A + B)
        elif item == '-':
            cal.append(A - B)
print("{:.2f}".format(cal.pop()))

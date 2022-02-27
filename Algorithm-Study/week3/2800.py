from itertools import combinations
import sys

def input():
    return sys.stdin.readline().rstrip()

problem = list(input())
p = []
idx= []
for i, v in enumerate(problem):
    if v == '(':
        problem[i] = ''
        p.append(i)
    elif v == ')':
        problem[i] = ''
        idx.append([p.pop(), i])

out = set()

for i in range(len(idx)):
    for j in combinations(idx, i):
        P = problem[:]
        for v, w in j:
            P[v] = '('
            P[w] = ')'
        out.add(''.join(P))
        
for item in sorted(out):
    print(item)
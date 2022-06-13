import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
heard = set(input() for _ in range(N))
heard_saw = []

for _ in range(M):
    s = input()
    if s in heard:
        heard_saw.append(s)

heard_saw.sort()
print(len(heard_saw))
for item in heard_saw:
    print(item)
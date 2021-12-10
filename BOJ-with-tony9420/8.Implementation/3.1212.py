import sys

def input():
    return sys.stdin.readline().rstrip()

print(format(int(input(), 8), 'b'))
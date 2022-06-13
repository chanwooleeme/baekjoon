import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
num_dict = {}

for item in list(map(int, input().split())):
    if not item in num_dict:
        num_dict[item] = 1
    else:
        num_dict[item] += 1

M = int(input())
for item in list(map(int, input().split())):
    if item in num_dict:
        print(num_dict[item], end = ' ')
    else:
        print(0, end = ' ')

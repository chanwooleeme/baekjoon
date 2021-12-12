import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

switch_list = [-1] + list(map(int, input().split()))
L = len(switch_list)
T = int(input())
for _ in range(T):
    gender, switch_num = map(int, input().split())
    if switch_num == 1:
        for i in range(switch_num, L, switch_num):
            switch_list[i] = int(not switch_list[i])
print(switch_list)
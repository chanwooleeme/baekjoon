import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

student_list = [0 for i in range(31)]
student_list[0] = 1
for _ in range(28):
    student = int(input())
    student_list[student] += 1
for i in range(1, 31):
    if student_list[i] == 0:
        print(i)

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
files = {}
for _ in range(n):
    s = input()
    idx = s.index('.')
    s = s[idx+1:]
    if s in files:
        files[s] += 1
    else:
        files[s] = 1
file_list = list(zip(files.keys(), files.values()))
file_list.sort()

for item in file_list:
    print(item[0], item[1])
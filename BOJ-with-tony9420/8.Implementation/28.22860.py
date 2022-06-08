import sys

sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

def search(target, fileSet):
    global fileCnt
    if target not in directory:
        return
        
    for title, id in directory[target]:
        if id == 0:
            if title not in fileSet:
                fileSet.add(title)
            fileCnt += 1
        else:
            search(title, fileSet)

N, M = map(int ,input().split())
directory = {}

for _ in range(N + M):
    From, To, Id = input().split()
    if From not in directory:
        directory[From] = []
    directory[From].append([To, int(Id)])

q = int(input())

for i in range(q):
    query = input().split('/')
    fileCnt = 0
    fileSet = set()
    search(query[-1], fileSet)
    print(len(fileSet), fileCnt)
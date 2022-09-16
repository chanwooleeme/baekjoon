import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    
    for _ in range(N):
        result = 1
        arr = []
        s = input()
        for item in s:
            if item == '(':
                arr.append(item)
            else:
                if arr:
                    arr.pop()
                else:
                    result = 0
                    break
        
        if arr or result == 0:
            print("NO")
        else:
            print("YES")

solution()
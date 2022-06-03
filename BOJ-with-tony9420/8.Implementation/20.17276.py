from copy import deepcopy
import sys

def input():
    return sys.stdin.readline().rstrip()

def turn_clockwise_45(n, arr):
    tmp = deepcopy(arr)
    
    for i in range(n):
        tmp[i][n//2] = arr[i][i]
        tmp[i][n-i-1] = arr[i][n//2]
        tmp[n//2][n-i-1] = arr[i][n-i-1]
        tmp[n-i-1][n-i-1] = arr[n//2][n-i-1]
        
    return tmp

def turn_counterclockwiese_45(n, arr): # i -> n - i - 1, n - i - 1 -> i
    tmp = deepcopy(arr)
    
    for i in range(n):
        tmp[n//2][i] = arr[i][i]
        tmp[n-i-1][i] = arr[n//2][i]
        tmp[n-i-1][n//2] = arr[n-i-1][i]
        tmp[n-i-1][n-i-1] = arr[n-i-1][n//2]
    
    return tmp

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    d %= 360
    if d > 180:
        d -= 360
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    if d >= 0:
        for _ in range(d // 45):
            arr = turn_clockwise_45(n, arr)
    else:
        for _ in range(-d // 45):
            arr = turn_counterclockwiese_45(n, arr)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
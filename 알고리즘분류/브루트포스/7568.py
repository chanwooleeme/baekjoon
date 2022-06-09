import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list([i] + list(map(int, input().split())) for i in range(n))
sorted_arr = sorted(arr, key=lambda x : (x[1], x[2]))

result = [0] * n

for i in range(n):
    cnt = 0
    idx, x1, y1 = sorted_arr[i]
    for j in range(i + 1, n):
        cur, x2, y2 = sorted_arr[j]
        if x1 < x2 and y1 < y2:
            cnt += 1
            
    result[idx] = cnt + 1
    
for item in result:
    print(item, end=' ')
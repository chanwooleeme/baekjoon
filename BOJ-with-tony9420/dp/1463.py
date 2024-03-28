import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    INF = int(1000000) + 1
    arr = [0 for _ in range(INF)]
    arr[0] = 0
    arr[1] = 0
    arr[2] = 1
    arr[3] = 1

    N = int(input())
    for i in range(4,INF):
        if i % 3 == 0 and i % 2 == 0:
            arr[i] = min(arr[i//3], min(arr[i//2], arr[i-1])) + 1
        elif i % 3 == 0:
            arr[i] = min(arr[i//3], arr[i-1]) + 1
        elif i % 2 == 0:
            arr[i] = min(arr[i//2], arr[i-1]) + 1
        else:
            arr[i] = arr[i-1] + 1
    
    print(arr[N])
    """
    0 0
    1 0
    2 1
    3 
    """
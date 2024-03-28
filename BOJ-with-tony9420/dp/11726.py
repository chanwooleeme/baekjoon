import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    arr = [0 for _ in range(1001)]
    arr[1] = 1
    arr[2] = 2
    arr[3] = 3
    arr[4] = 5
    for i in range(5, 1001):
        arr[i] = (arr[i-1] + arr[i-2]) % 10007
    print(arr[N])
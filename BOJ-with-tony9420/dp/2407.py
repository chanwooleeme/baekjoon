import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n, r = map(int, input().split())
    fac = [0 for _ in range(101)]
    fac[0] = 0
    fac[1] = 1
    fac[2] = 2
    for i in range(3, 101):
        fac[i] = fac[i-1] * i
    
    print(fac[n] // (fac[n-r] * fac[r]))
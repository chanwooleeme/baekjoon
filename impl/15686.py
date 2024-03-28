import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N, M = map(int, input().split())
    houses = list()
    chickens = list()
    for i in range(N):
        inputs = list(map(int, input().split()))
        for j in range(len(inputs)):
            if inputs[j] == 1:
                houses.append([i, j])
            elif inputs[j] == 2:
                chickens.append([i, j])
    
    result = 10e9
    

    for combs in combinations(chickens, M):
        for c in combs:
            tmp = 0
            for house in houses:
                print(c, house)
                tmp += (abs(c[0] - house[0]) + abs(c[1] - house[1]))
            result = min(result, tmp)
            print()
    print(result)

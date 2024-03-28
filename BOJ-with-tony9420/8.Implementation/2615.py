import sys


def input():
    return sys.stdin.readline().rstrip()


def is_omok(li: list):
    for xy in li:
        x = xy[0]
        y = xy[1]
        
if __name__ == '__main__':
    board = list()
    result = 0
    list_1 = []
    list_2 = []

    for i in range(19):
        inputs = list(map(int, input().split()))
        for j in range(len(inputs)):
            if inputs[j] == 1:
                list_1.append([i, j])
            elif inputs[j] == 2:
                list_2.append([i, j])
    
    print(list_1)
    print(list_2)

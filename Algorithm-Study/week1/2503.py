import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

def validate(input_item: list, item: tuple):
    num, strike, ball = input_item
    num = str(num)
    
    s = 0
    b = 0
    for i in range(3):
        n = int(num[i])
        if n in item:
            if item.index(n) == i:
                s += 1
            else:
                b += 1
    if s == strike and b == ball:
        return True
    return False
       
data = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

result = 0
input_list = []

for _ in range(int(input())):
    input_list.append(list(map(int, input().split())))
    
for item in data:
    flag = True
    for input_item in input_list:
        if not validate(input_item, item):
            flag = False
            break
    if flag:
        result += 1

print(result)
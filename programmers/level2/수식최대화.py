from itertools import permutations

def calculate(li, opr):
    while opr in li:
        i = li.index(opr)
        if opr == '*':
            num = li[i-1] * li[i+1]
        elif opr == '+':
            num = li[i-1] + li[i+1]
        elif opr == '-':
            num = li[i-1] - li[i+1]
        li = li[:i-1] + [num] + li[i+2:]
    return li

def split(expression):
    li = []
    tmp = ""
    for c in expression:
        if c.isdigit():
            tmp += c
        else:
           li.append(int(tmp))
           li.append(c)
           tmp = ""
    li.append(int(tmp))
    return li
    
def solution(expression:str):
    answer = 0
    li = split(expression)
    for item in list(permutations(['*', '+', '-'], 3)):
        _li = calculate(li, item[0])
        _li = calculate(_li, item[1])
        _li = calculate(_li, item[2])
        answer = max(answer, abs(_li[0]))
    return answer

print(solution("100-200*300-500+20"))
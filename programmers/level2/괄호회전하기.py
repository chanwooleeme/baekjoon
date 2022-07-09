from collections import deque

def is_correct(q:deque):
    stack = []
    for item in q:
        if item == '[' or item == '(' or item == '{':
            stack.append(item)
        elif item == ']' or item == ')' or item == '}':
            if not stack:
                return False
            if item == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif item == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif item == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    q = deque(list(s))
    for _ in range(len(s)):
        if is_correct(q):
            answer += 1
        q.rotate(-1)
    return answer

solution("}]()[{")
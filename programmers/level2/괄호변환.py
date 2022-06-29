def is_balanced(u:str):
    if u.count('(') == u.count(')'):
        return True
    return False

def is_correct(u:str):
    stack = []
    for c in u:
        if not stack:
            stack.append(c)
        else:
            if c == ')':
                stack.pop()
            else:
                stack.append(c)
    if stack:
        return False
    return True

def split(p):
    u, v = '', ''
    for i in range(2, len(p) + 2, 2):
        u, v = p[:i], p[i:]
        if is_balanced(u):
            break
    if not u:
        return ''
    if is_correct(u):
        if not v:
            return u
        return u + split(v)
    else:
        s = '(' + split(v) + ')'
        for item in u[1:-1]:
            if item == ')':
                s += '('
            else:
                s += ')'
        return s
        
def solution(p):
    if not p:
        return ''
    return split(p)
    
solution("()))((()"	)
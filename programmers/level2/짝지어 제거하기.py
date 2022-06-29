def solution(s):
    stack = []
    for item in s:
        if not stack:
            stack.append(item)
        else:
            if stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)
    if stack:
        return 0
    return 1

print(solution("baabaa"))
print(solution("abcda"))
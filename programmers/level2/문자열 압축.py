def zip(li):
    result = ""
    cnt = 1
    for i in range(1, len(li)):
        if li[i - 1] == li[i]:
            cnt += 1
        else:
            if cnt == 1:
                result += li[i -1]
            else:
                result += str(cnt)
                result += li[i - 1]
                cnt = 1
    if cnt != 1:
        result += str(cnt)
    result += li[-1]
        
    return len(result)
        
def split(s, l):
    li = []
    for i in range(0, len(s), l):
        li.append(s[i:i+l])
    return li
            
def solution(s):
    answer = 10e9
    for l in range(1, len(s) + 1):
        answer = min(answer, zip(split(s, l)))
    return answer

solution("aabbaccc")
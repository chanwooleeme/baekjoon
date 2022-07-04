def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for i in s:
        li = i.split(',')
        for j in li:
            if int(j) not in answer:
               answer.append(int(j))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))
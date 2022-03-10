s = "aabbaccc"
answer = len(s)
for i in range(1, len(s)):
    tmp = []
    result = ""
    # 일단 자르고
    for j in range(0, len(s), i):
        tmp.append(s[j:i+j])
    # 잘린게 같은지 확인
    sep_list = []
    cur = []
    for t in tmp:
        if not cur:
            sep_list.append(1)
            sep_list.append(t)
            cur = t
        else:
            if cur == t:
                sep_list.pop()
                v = sep_list.pop()
                sep_list.append(v + 1)
                sep_list.append(t)
            else:
                cur = t
                sep_list.append(1)
                sep_list.append(t)
    sep_list = list(map(str, sep_list))
    for item in sep_list:
        if item != '1':
            result += item
    answer = min(answer, len(result))
print(answer)
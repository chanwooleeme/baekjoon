def solution(record):
    answer = []
    id_dict = dict()
    q = list()
    for data in record:
        li = data.split()
        if li[0] == "Enter":
            id_dict[li[1]] = li[2]
            q.append((0, li[1]))
        elif li[0] == 'Leave':
            q.append((1, li[1]))
        else:
            id_dict[li[1]] = li[2]
    for item in q:
        status, uid = item
        nickname = id_dict[uid]
        if status == 0:
            answer.append(nickname + "님이 들어왔습니다.")
        else:
            answer.append(nickname + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
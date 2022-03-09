def solution(id_list, report, k):
    answer = []
    n = len(id_list)

    table = [[] for _ in range(n)]
    dictionary = dict()
    reported_dict = dict()
    reject = []
    
    for idx, id in enumerate(id_list):
        dictionary[id] = idx
        reported_dict[id] = 0
    
    for data in report:
        user, reported = data.split()
        
        if not reported in table[dictionary[user]]:
            table[dictionary[user]].append(reported)
            reported_dict[reported] = reported_dict[reported] + 1

        if reported_dict[reported] >= k:
            reject.append(reported)
        
    reject = list(set(reject))
    for data in table:
        cnt = 0
        for d in data:
            if d in reject:
                cnt += 1
        answer.append(cnt)
    return answer
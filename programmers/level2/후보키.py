from itertools import combinations

def solution(relation):
    r = len(relation)
    c = len(relation[0])
    
    combi = []
    for i in range(1, c + 1):
        combi.extend(combinations(range(c), i))
    
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == r:
            flag = True
            
            for x in unique:
                if set(x).issubset(set(i)):
                    flag = False
                    break
            if flag:
                unique.append(i)
    return len(unique)
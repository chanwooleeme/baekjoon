from itertools import combinations

def combine(orders, course):
    iter = 0
    result = []
    for order in orders:
        iter = max(iter, len(order))
    

    for i in range(2, iter + 1):
        menu = dict()
        for order in orders:
            order = sorted(order)
            for item in list(combinations(list(order), i)):
                if item in menu:
                    menu[item] += 1
                else:
                    menu[item] = 1
                    
        for data in [k for k, v in menu.items() if max(menu.values()) == v and v >= 2]:
            s = ""
            for char in data:
                s += char
            for c in course:
                if len(s) == c:
                    result.append(s)
    result.sort()
    return result
    
        
def solution(orders, course):
    return combine(orders, course)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	,[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
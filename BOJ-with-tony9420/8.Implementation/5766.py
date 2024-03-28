import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        rank_dict = dict()
        for _ in range(N):
            for key in map(int, input().split()):
                if key in rank_dict:
                    rank_dict[key] += 1
                else:
                    rank_dict[key] = 1
        
        result_list = []
        second_score = sorted(rank_dict.values())[-2]
        for key, val in rank_dict.items():
            if val == second_score:
                result_list.append(key)
        result_list = sorted(result_list)
        
        print(' '.join(map(str, result_list)))

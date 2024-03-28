import sys

def input():
    return sys.stdin.readline().rstrip()


def dfs():
    return

if __name__ == '__main__':
    N = int(input())
    answer = [0 for _ in range(N)]
    routes = input()
    answer_list = list()
    for i in range(N):
        cur = i
        flag = False
        visited = [False for _ in range(N)]
        while True:
            if routes[cur] == 'E':
                visited[cur] = True
                cur += 1
                if visited[cur] == True:
                    answer_list.append([cur-1, cur])
                    break
            else:
                visited[cur] = True
                cur -= 1
                if visited[cur] == True:
                    answer_list.append([cur, cur+1])
                    break
    print(len(list(set(tuple(sublist) for sublist in answer_list))))
    
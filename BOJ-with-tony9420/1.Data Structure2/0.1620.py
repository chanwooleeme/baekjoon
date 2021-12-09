import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pokemon_dic = {}
for i in range(1, N+1):
    pokemon = input()
    pokemon_dic[i] = pokemon
    pokemon_dic[pokemon] = i
for _ in range(M):
    val = input()
    if val.isdigit():
        print(pokemon_dic[int(val)])
    else:
        print(pokemon_dic[val])
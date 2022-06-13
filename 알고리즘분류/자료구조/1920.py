N = int(input())

# num_dict = {}
# for item in list(map(int, input().split())):
#     num_dict[item] = True

# n = int(input())
# for item in list(map(int, input().split())):
#     if item in num_dict:
#         print(1)
#     else:
#         print(0)
num_set = set(map(int, input().split()))
n = int(input())
for item in list(map(int, input().split())):
    if item in num_set:
        print(1)
    else:
        print(0)
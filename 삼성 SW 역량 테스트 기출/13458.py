N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for student in A:
    cnt = 1
    student -= B
    if student <= 0:
        result += cnt
        continue
    if not student % C:
        cnt += (student // C)
    else:
        cnt += (student // C + 1)
    result += cnt
    
print(result)
        
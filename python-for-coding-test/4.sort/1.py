"""
K번의 바꿔치기 : 
배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서
두 원소를 서로 바꾸는것
목표 : 배최대 K번 바꿔치기를 해서 배열 A의 모든 원소의 합이 최대
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
	else:
		break
print(sum(a))
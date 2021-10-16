n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_val = cities[0]
result = 0
for i in range(n - 1):
	if cities[i] < min_val:
		min_val = cities[i]
	result += (min_val * roads[i])
print(result)
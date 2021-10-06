# """
# 기준 데이터(Pivot)을 설정하고 그 기준보다 큰 데이터와
# 작은 데이터의 위치를 바꾸는 방법
# """

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def my_quick_sort(arr, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end
	while (left < right):
		while(left <= end and arr[left] <= arr[pivot]):
			left += 1
		while(right > start and arr[right] >= arr[pivot]):
			right -= 1
		if left > right:
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:
			arr[left], arr[right] = arr[right], arr[left]
	my_quick_sort(arr, start, right - 1)
	my_quick_sort(arr, right + 1, end)

my_quick_sort(test_arr, 0, len(test_arr) - 1)
print(test_arr)

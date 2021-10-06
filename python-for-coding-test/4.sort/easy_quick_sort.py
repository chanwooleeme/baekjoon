arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def my_easy_quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	tail = arr[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return my_easy_quick_sort(left_side) + [pivot] + my_easy_quick_sort(right_side)

result = my_easy_quick_sort(arr)
print(result)
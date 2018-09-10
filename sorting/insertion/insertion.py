def insertion_sort(unsorted_list):
	for index in range(1, len(unsorted_list)):
		current_value = unsorted_list[index]
		pos = index
		while pos > 0 and unsorted_list[pos - 1] > current_value:
			unsorted_list[pos] = unsorted_list[pos - 1]
			pos -= 1
		unsorted_list[pos] = current_value


test_list = [3, 7, 5, 1, 8, 3, 9, 6, 2]
print("unsorted list")
print(test_list)
print("sorted list")
insertion_sort(test_list)
print(test_list)

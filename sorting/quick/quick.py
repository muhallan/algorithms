def quick_sort_interface(list_to_sort):
	quick_sort(list_to_sort, 0, len(list_to_sort) - 1)


def quick_sort(unsorted_list, start_index, end_index):
	if start_index < end_index:
		partition_index = partition(unsorted_list, start_index, end_index)
		quick_sort(unsorted_list, start_index, partition_index - 1)
		quick_sort(unsorted_list, partition_index + 1, end_index)


def partition(list_to_sort, low_index, high_index):
	divider = low_index
	pivot = high_index

	for index in range(low_index, high_index):
		if list_to_sort[index] < list_to_sort[pivot]:
			list_to_sort[index], list_to_sort[divider] = list_to_sort[divider], list_to_sort[index]
			divider += 1
	list_to_sort[divider], list_to_sort[pivot] = list_to_sort[pivot], list_to_sort[divider]

	return divider


# testing
print("unsorted list")
my_list = [3, 5, 2, 1, 11, 14, 6, 5, 0, 4]
print(my_list)
quick_sort_interface(my_list)
print("sorted list")
print(my_list)

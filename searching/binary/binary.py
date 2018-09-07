def binary_search(list_to_search, item):
	start = 0
	end = len(list_to_search) - 1
	found = False
	while start <= end and not found:
		middle = (start + end) // 2
		if list_to_search[middle] == item:
			found = True
		else:
			if item < list_to_search[middle]:
				end = middle - 1
			else:
				start = middle + 1
	return found


def binary_search_recursive(list_to_search, item):
	if len(list_to_search) == 0:
		return False
	else:
		midpoint = len(list_to_search) // 2
		if list_to_search[midpoint] == item:
			return True
		else:
			if item < list_to_search[midpoint]:
				return binary_search_recursive(list_to_search[:midpoint], item)
			else:
				return binary_search_recursive(list_to_search[midpoint + 1:], item)


# testing non recursive
even_nums = [2, 4, 6, 8, 10]
print(" -- non recursive --")
# find 5
print(binary_search(even_nums, 5))
# find 4
print(binary_search(even_nums, 4))

# testing recursive
print(" -- recursive --")
# find 5
print(binary_search_recursive(even_nums, 5))
# find 4
print(binary_search_recursive(even_nums, 4))

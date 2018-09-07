def sequential_search(list_to_search, item):
	found = False
	index = 0
	while index < len(list_to_search) and not found:
		if list_to_search[index] == item:
			found = True
		else:
			index += 1
	return found


# testing
even_nums = [2, 4, 6, 8, 10]
# find 5
print(sequential_search(even_nums, 5))
# find 4
print(sequential_search(even_nums, 4))

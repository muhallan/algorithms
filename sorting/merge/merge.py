def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        merge_sort(left_list)
        merge_sort(right_list)
        merge_lists(left_list, right_list, unsorted_list)


def merge_lists(left_list, right_list, merged_list):
    left_index = right_index = merged_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            merged_list[merged_index] = left_list[left_index]
            left_index += 1
        else:
            merged_list[merged_index] = right_list[right_index]
            right_index += 1

        merged_index += 1

    while left_index < len(left_list):
        merged_list[merged_index] = left_list[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_list):
        merged_list[merged_index] = right_list[right_index]
        right_index += 1
        merged_index += 1


# testing
print("unsorted list")
my_list = [3, 6, 6, 2, 5, 8, 43, 78, 34, 86, 34, 65, 23, 46, 63, 753, 24, 85, 9, 342, 785, 23, 3, 24, 643, 24]
print(my_list)
merge_sort(my_list)
print("sorted list")
print(my_list)

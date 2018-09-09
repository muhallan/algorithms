def bubble_sort(list_to_sort):
    for pass_number in range(len(list_to_sort)-1, 0, -1):
        for i in range(pass_number):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]


# testing
test_list = [5, 6, 2, 67, 832, 5, 884, 1, 3, 553, 6, 112, 5778, 23246, 578, 32, 53, 1, 2, 333, 52, 1, 2, 134, 167, 353, 67, 22, 2, 22, 75, 83, 32]
bubble_sort(test_list)
print(test_list)

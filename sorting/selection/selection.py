def selection_sort(unsorted_list):
    for slot_to_fill in range(len(unsorted_list) - 1, 0, -1):
        biggest_num_pos = 0
        for pos in range(1, slot_to_fill + 1):
            if unsorted_list[pos] > unsorted_list[biggest_num_pos]:
                biggest_num_pos = pos
        unsorted_list[slot_to_fill], unsorted_list[biggest_num_pos] = unsorted_list[biggest_num_pos], unsorted_list[slot_to_fill]


my_list = [3, 5, 7, 2, 23, 1, 67, 84, 23, 24, 85, 12, 67, 35, 87, 21, 8, 12]
print("unsorted list")
print(my_list)
selection_sort(my_list)
print("sorted list")
print(my_list)

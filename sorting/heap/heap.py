import heapq


def heap_sort(iterable):
    my_heap = []
    for value in iterable:
        heapq.heappush(my_heap, value)
    heapq.heapify(my_heap)
    return [heapq.heappop(my_heap) for _ in range(len(my_heap))]


unsorted_list = [5, 23, 1, 56, 62, 2, 4, 9, 13, 21, 92, 73, 12]
print("unsorted list:")
print(unsorted_list)
print("sorted list:")
print(heap_sort(unsorted_list))

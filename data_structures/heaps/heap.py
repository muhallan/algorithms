import heapq

# original list to convert to heap
heap = [3, 5, 4, 9, 12, 1, 5, 8, 17, 35, 23, 16]
print("-- original list")
print(heap)

# convert it to a heap
heapq.heapify(heap)
print("-- resulting heap --")
print(heap)

# add an element to the heap
heapq.heappush(heap, 11)
print("-- add 11 to the heap --")
print(heap)

# remove an element from the heap
print("-- pop an element from the heap -- We've popped:", end=' ')
print(heapq.heappop(heap))
print(heap)

# replacing an element in a heap
print("-- remove the smallest element and add 7 -- We've popped:", end=' ')
print(heapq.heapreplace(heap, 7))
print(heap)

# push an element and then pop
print("-- push 2 and the pop the smallest element -- We've popped:", end=' ')
print(heapq.heappushpop(heap, 14))
print(heap)

# get the largest 4 elements
print("-- the largest 4 elements are: ", end='')
print(heapq.nlargest(4, heap))
print(heap)

# get the smallest 5 elements
print("-- the smallest 5 elements are: ", end='')
print(heapq.nsmallest(5, heap))
print(heap)


def heap_sort(iterable):
    my_heap = []
    for value in iterable:
        heapq.heappush(my_heap, value)
    return [heapq.heappop(my_heap) for i in range(len(my_heap))]


unsorted_list = [5, 23, 1, 56, 62, 2, 4, 9, 13, 21, 92, 73, 12]
print("unsorted list:")
print(unsorted_list)
print("sorted list:")
print(heap_sort(unsorted_list))

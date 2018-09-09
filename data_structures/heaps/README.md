# Heaps
A heap is a tree structure where each parent node is less than or equal to
its child node. When it's like this, it's then called a **min heap**. But also
the parent node can be greater than or equal to its child node. This one is then
called a **max heap**. Whenever elements of a heap are pushed or popped,
the heap structure is always maintained. The root element of a heap, `heap[0]`
always returns the smallest element each time, if it's a min heap, that is.

In Python a heap is implemented using an inbuilt library called `heapq`.
This is also called a heap queue. Among its functions are these listed below;

* `heapify(iterable)` - converts a regular iterable to a heap structure.
In the resulting heap the smallest element gets pushed to the index position 0.
But rest of the data elements are not necessarily sorted. The elements are
arranged in a heap order.
* `heappush(heap, element)` – adds an element to the heap without altering the current heap.
The order is adjusted to maintain the heap structure.
* `heappop(heap)` - removes and returns the smallest data element from the heap.
The order is adjusted to maintain the heap structure. To access the
smallest item without popping it, use `heap[0]`.
* `heapreplace(heap, element)` – replaces the smallest data element with a
 new value supplied in the function. Here the existing element is first popped,
 then the new element is pushed.
* `heappushpop(heap, element)` - the element supplied is pushed to the heap
and then the smallest element is popped. Pushing happens before popping.
* `nlargest(k, iterable[, key])` - returns the k largest elements from
 the iterable specified and key, if provided, specifies a function of
 one argument that is used to extract a comparison key from each element in the iterable.
* `nsmallest(k, iterable[, key])` - return the k smallest elements from
the iterable specified and key, if provided, specifies a function of
 one argument that is used to extract a comparison key from each element in the iterable.

## Application
A priority queue is a common use case for a heap. This can be used to define
and sort tasks based on their priorities.

It can also be used for implementing schedulers like for when events are
supposed to run.

They can also be used in sports tournament applications where there is a
hierarchy of participants with the winner on top.
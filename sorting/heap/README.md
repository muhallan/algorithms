# Heap Sort
Heap sort is a comparison based sorting technique based on a binary heap data structure.
It is similar to selection sort where we first find the maximum element and place
the maximum element at the end. We repeat the same process for remaining elements.

Since heaps must always follow a specific order, we can leverage that property and
use that to find the smallest, minimum value element, and sequentially sort
elements by selecting the root node of the heap (min heap), and adding it to the start of the array.

After popping the smallest element of the heap, the heap is reorganized to maintain the heap structure.
The sorting ends when all the items have been popped from the heap.

## Complexity
Heap sort has **O(nlogn)** time complexities for all the cases (best case, average case and worst case).
It performs sorting in **O(1)** space complexity.

## Analysis
Heap sort is an in-place sorting algorithm. Because of the nature of heaps and the heapify function,
if there are duplicate elements, we can’t rely on elements maintaining their order! So, heap sort is unstable.


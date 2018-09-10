# Selection Sort
Selection sort uses almost the same logic as bubble sort but with the exception
that it does only one swap of elements for each pass through the
collection.

Same as bubble sort, after the first pass, the largest element is in its proper
place, that is, at the end. In the second pass, the second largest element is
also placed at the second last position. This happens until the whole collection
is exhausted.

The only swap happens when placing the biggest element in its proper position
for that pass. The element that was in that position is placed in the position
where that biggest element was. At the end of all the passes, the collection is
sorted.

## Complexity
The number of passes to sort a collection of **n** items is **n - 1**. This makes
selection sort to make the same number of comparisons of elements as bubble sort which is
the sum of the first **n - 1** integers.

This results in a complexity of **0(n^2)**.

## Analysis
Selection sort reduces the number of swaps for elements. This makes it to run
faster than bubble sort.

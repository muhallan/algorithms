# Quick Sort
Quick sort also uses the principle of divide and conquer to recursively sort sub-lists of the original
list until the whole list is sorted. How it does this, it uses a technique called partitioning which is
the gist of the algorithm. It is represented by the `partition()` function in our implementation.

The essence of partitioning is to divide the list into two lists based on a point that contains an
element that is in its proper sorted position in the original list. We call this point a `partition_index`.
Every element before the partition element is smaller than it and every element after the partition index is
larger than it. This makes the element in the partition index sorted.

After getting the `partition_index`, the list is divided into two sub-lists, one to the right of that index
and another to its left. Each of those lists then go through the same process of getting their partition index
and then subdividing itself. This recursion stops when the list to be subdivided contains only one element.
That element is considered to be in its sorted position.

The left side of the partition index is subdivided until it's all sorted, then control goes to the right
side of the list as well. At the end of it all, the whole list is sorted.

The `partition()` function where the sorting operation works, is heavily based on the choice of a value
called the `pivot`. This `pivot` is used in assisting in dividing/partitioning the list. The position of the
pivot is what is called the partitioning index, and that's what's used to divide the list further in the next
quick sort recursive call. This makes choice of the pivot value very vital to size of the subdivided lists. In
our implementation, we use the last value as the pivot value. Other implementations can use the first value
and others the `median of three`. Each of these tweaks the implementation of the `partition()` function to suit it.
The `pivot` value is the one that is used to move elements around such that elements less than that value are
before it and those that are greater than it are to its right.

## Complexity
Complexity can vary for the best case, average case and worst case scenarios. The best case occurs when
the partition process picks the middle element as the `pivot`. Here for a list of length `n`, there will be
`log n` divisions. When finding the partition index, each of the `n` times will have to be checked against
the pivot. This results in the complexity of `O(n log n)`.

In the worst case, the partition process always picks the greatest or the least element as the `pivot`. Also
the worst case can occur when the list is already sorted. This results in the complexity of `O(n^2)`.

The average case gives a complexity of `O(n log n)`.

## Analysis
The complexity of quick sort largely depends on the selection of the `pivot` value. This is due to the
potential for uneven division of the list. Quick sort is faster in practice because its inner loop can be
efficiently implemented on most architectures and in most real world data.

Also quick sort is an `in-place` sort which means that it doesn't require any extra storage space to
execute. This is because the original list is what is used to sort it. Data is simply moved around the
indices. Comparing quick sort with merge sort, merge sort uses extra storage, to store each of the sub-lists it creates
and this is quite expensive. Allocating and de-allocating the extra space used for merge sort
increases the running time of the algorithm which is not needed for quick sort.
Comparing average complexity, both sorts have `O(n logn )` average complexity but the constants differ
in favor of quick sort.

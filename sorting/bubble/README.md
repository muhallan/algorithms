# Bubble Sort
Bubble sort is a sorting mechanism that sorts elements of a collection
by various passes through the collection while in each pass, it does comparisons
of adjacent items adjusting them according to the required order, whether
ascending or descending. If it's ascending, after every pass, the largest
item is placed in it's proper place at the end of the list. It's called
bubble sort because each item moves up the list, bubbling to the place where
it belongs.

The number of passes needed to properly sort a collection are equal to
**n - 1** where **n** represents the number of items in the collection.
Bubble sort happens due to the exchanging of adjacent values in case they are
out of order.

## Complexity
Regardless of how items are arranged in the initial list, there will be
**n - 1** passes to sort a collection of size **n**. The total number of
comparisons is the sum of the first **n - 1** integers.

This is equivalent to **1/2(n^2) - 1/2(n)**. This is **O(n^2)** comparisons.
In the best case, if the list is already ordered, no exchanges will be made.
In the worst case, every comparison will cause an exchange. On average,
half the exchanges will be made. However complexity is **O(n^2)**.

## Analysis
Bubble sort is very inefficient since it must exchange all items since before
the final location is known. These exchanges are memory intensive and time
consuming.

However an advantage of bubble sort is that since it makes passes through the
whole list, it can tell whether the list is sorted if there are no exchanges in a
particular pass. If that's the case, then the algorithm can be modified to
stop early.

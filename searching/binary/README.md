# Binary search
If we are dealing with an ordered list, then binary search is much more effective to help us search for an item.
With binary search, we start by checking the middle item.

If it's what we want, we stop, else, we check if the item we want is less than the middle item. With this, we eliminate one half of the
collection. If it is less, then we take the first half, else we take the second half. Then we again check the middle item, and do this repeatedly until
either we've exhausted the whole list or we find the item we are looking for.

This an example of the **Divide and conquer** strategy. This algorithm can also be implemented using a recursive function, since for every
iteration, we do the same thing until when the list is empty.

## Complexity
If we have n items, about n/2 items will be left after the first comparison, then about n/4 after the second, then n/8, n/16, and so on.
When we split the collection enough times, we end up with a collection with just one item. That's either the item we want or not, but that's the last comparison.

The number of comparisons / iterations necessary to get to this point is i where n/(2^i) = 1.
Solving for i gives us i = log n.

The maximum number of comparisons is the logarithm of the number of items in the list.
Therefore, the binary search complexity is **O(log n)**.

## Use case
Binary search is useful if you have a sorted list. If your list is not sorted, it might be more slower and computationally expensive
to first sort the list and then search it. This is especially true for large lists. For small lists, the advantage of binary search
might not be much compared to sequential search.

But if you're going to search multiple times, it might be worth it to sort once, and the do your searches multiple times using
binary search.

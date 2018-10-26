# Sequential search
This kind of search goes through all the elements of a collection in a sequence checking each element if it's equal to the item
being search for. If the item is found, then the search is complete.

If the item is not in the list, then all the elements will be traversed.

It's called sequential search because indices of a collection are ordered, and hence it is possible for us to visit them in sequence
starting from zero to the last index which is equal to length of the collection minus 1.

## Complexity
In the best case we will find the item in the first place we look, at the beginning of the list. We will need only one comparison. In the worst case, we will not discover the item until the very last comparison, the nth comparison.

On average, we will find the item about halfway into the list; that is, we will compare against n/2 items.
However, as n gets large, the coefficients, no matter what they are, become insignificant in our approximation, so the complexity of the sequential search, is **O(n)**.

`n` stands for the length of the collection of items.

## Use case
Sequential search can be used when the data set is relatively small and can be traversed through quickly.

Also it can be used when the data is not ordered.

It's also relatively simple to implement.
# Insertion Sort
Insertion sort works by maintaining a sorted sublist on the left hand side of the list
and then for every pass, it gets an element from the right and inserts into its required
position in the left sublist, maintaining its sorted structure.

We begin the sorted list with the first element, and then we keep bringing an extra element from the right
hand side and comparing it with the items already in the sorted list. Items that are bigger the item we are
comparing with are shifted to the right until we reach the end of the list or a smaller item is encounter and
the carried item is inserted in that position.

This means that for every pass, the sorted list keeps growing bigger until we reach the end of the list
and every element has been brought to the left and the whole list is now sorted.

## Complexity
There are **n - 1** passes to sort *n* items in a list. This algorithm starts
at position 1 and moves through positions n - 1 moving items into the sorted
sublist.

The maximum number of comparisons done for an insertion sort is the sum of the
first **n - 1** integers. The complexity for this algorithm is **O(n^2)**

In the best case, for a sorted list, only one comparison is done per pass.

## Analysis
When an item is encountered that is bigger than the current item being
compared, the bigger item is moved in front and it leaves an empty slot behind for
insertion of the smaller item being moved. This operation is called shifting and not
swapping / exchanging as is done in bubble sort.

Generally shifting items is not computational intensive as exchanging items because
only one assignment is done as opposed to two for exchanging. This makes
makes insertion sort have a better performance.

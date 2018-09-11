# Merge Sort
Merge sort works using the principle of divide and conquer where a problem is
divided into multiple small problems and then each problem is solved independently
and the solutions later make up the solution of the bigger problem.

Merge sort does this by dividing the unsorted list into multiple small lists recursively until each list has
one element. A list of one element is considered sorted. This division happens through
a function that splits up a list given to it into two parts, the left and the right.
The left list is fed back into the function recursively until the list created has only element,
then execution goes onto the right list as well splitting it until one element.

Once both the right and left lists have one element each, a function to merge the two
lists is called. During merging, the items in the two lists are compared and then
merged in a sorted manner.

After merging, the execution goes back to the earlier function call (the previous recursive one) which is now
executing on the other sublist. At the end of it all, all halved lists merge back together
when they are sorted and the algorithm completes.

In the algorithm shown, the merging function puts back the sorted items one at a time
into the original list so that at the end of it all, that list has sorted elements.

## Complexity
There are two distinct processes in the operation of merge sort. These are splitting
the lists into halves and merging the lists.

Splitting a list into half take **log n** times when **n** is the length of the list.

Merging takes **n** operations for a list of size **n** because every element will eventually
be compared and added back to the sorted list.

This means that there are **log n** splits each of which costs **n** which a total of **n log n**
operations.

As a result merge sort has a complexity of **O(n log n)**.

## Analysis
Merge sort has a worst case complexity of **O(n log n)** which makes it significantly faster than some other sorting
algorithms. Though it's worth noting that since this algorithm splits up a list into multiple
small lists, each of these lists will need to be stored somewhere in memory. This extra needed space
can be critical if the data set is very large and it can be a cause of problems.

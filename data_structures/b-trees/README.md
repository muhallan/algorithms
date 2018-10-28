# B-Trees
A B-Tree is a self - balanced search tree with multiple keys in every node and more
than one child for every node.

The number of keys and the number of children for a node in a B-Tree depend on its
**order**.

A B-Tree of order `m` has the following properties;
- Every node has at most `m` children
- A non-leaf node with `k` children contains `k - 1` keys. For any given node,
you have one more children than the number of keys. Also any node cannot have
more than `m - 1` keys.
- The root has at least two children if it's not a leaf node
- Every non-leaf node except the root has at least the ceiling of `m/2` children
- All leaves appear in the same level
- B-Trees are created from the bottom - up
- All the key values within a node must be in ascending order. The child between two keys k1 and k2 contains all keys in the range from k1 to k2.
- Time complexity to search, insert and delete is **O(log n)**

## Search operation in a B-Tree
The search process starts from the root node but every time we make an `n-way` decision where
`n` is the total number of children that the node has. The search operation is performed
in these steps;
1. Let the element to search for be `k`
1. Compare `k` with the first key value of the root
1. If the two are matching, then the value is found. Terminate the function
1. If the two are not matching, check whether `k` is greater or smaller than that
key value.
1. If it is smaller, then go to the left subtree and compare again
1. If it is greater, then compare with the next key value in the node. Repeat the process
in 3, 4, 5, and 6 until the element is found or until we reach the last key value
in the leaf node
1. If we reach the last element in the leaf node, then the element in not found.
Terminate the function

## Insertion operation in a B-Tree
A new element is always inserted at a leaf node. The insertion process happens in the
following steps;
1. Check if the tree is empty
1. If the tree is empty, create a new node with the key node and insert it into
the tree as the node
1. If the tree is not empty, find the leaf node to which the new key can be added.
This is got by checking if the key of the new node is less than or larger
than the keys in the root. When the position where it belongs is found, it is either
moved to the left subtree if it is smaller/equal or the right subtree if it is larger
than the comparing key.
1. If that found leaf node is already full, then split that leaf node by sending
the middle value to its parent node. Keep doing this until the value we've sent
up is fixed in a node.
1. If we split the root node, then the middle value becomes the new root node for
the tree and the height of the tree is increased by one.

## Application of B-Trees
B-Trees are used in placing and locating files in a database. The B-tree
algorithm minimizes the number of times a medium must be accessed to locate a desired record,
thereby speeding up the process.

B-Trees are also used in filesystems to allow quick random access to an arbitrary block
of data in a particular file.

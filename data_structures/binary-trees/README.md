# Binary Trees
A `tree` is a non-linear data structure that has nodes that are connected by edges. One node which is the
topmost node is called the `root`. This is the one without a `parent`. Every other node has one parent. Each
node can have an arbitrary number of `children`. Nodes with no children are called `leaves`.

A `binary tree` is a tree whose nodes have utmost 2 children. These are typically named `right child` and `left child`.

There are various types of binary trees. Some are discussed below:
* Full binary tree. This a binary tree where every node has two children except leaves which have no children at all.
* Complete binary tree. This is a binary tree where all levels are completely filled except possibly the last level. And if the last level
is not completely filled, then the children are all as left as possible.
* Perfect binary tree. This is a binary tree where all the internal nodes have two children and all leaves are at the same level.
* Balanced binary tree. A balanced binary tree is one whose height is **O(log n)** where **n** is the number of nodes.
* Degenerate or pathological tree. This is one where every internal node has one child.
* Extended binary tree. This is a tree that adds dummy nodes to become a full binary tree.

## Binary tree traversal
Binary tree traversal is the order of display or visiting of nodes in a binary tree.

There are two kinds of tree traversals:

**Breadth First or Level Order Traversal**

This starts at the root of the tree and then explores the neigboring nodes at the current depth/level before moving on
to the nodes at the next depth level. The order of traversal at the given level is left node first, then right node.

**Depth First Traversal**

This starts at the root node and explores as far as possible along a given branch before moving back up until all the nodes are visited.

There are three types of this kind of traversal.

1. In-order traversal (leftChild - root - rightChild)

   In this traversal, the left child is visited first, then the root node is visited and then the right node. This kind of in-order traversal is done
   for all the subtrees in the tree. This is done recursively for all nodes of the tree. We start by visiting the left child of the root, but if we find that left
   child is a root for other nodes, then we go to its left child as well. This continues until we find the leftmost child, i.e. the last one. We then visit that
   one, then go for its root and then go to the right child of this root. That makes the complete left side of the next root from the bottom. Then we go to the
   right child of that root. We then go left until we reach the end, then to the root and back to the right. This is done for all the nodes on the left side, then
   we go to the right side, and do the same until the whole tree is traversed.

   In case of binary search trees (BST), In-order traversal gives nodes in a non-decreasing order.

2. Pre-order traversal (root - leftChild - rightChild)

   In this traversal, the root node is visited first, then its left child and then the right child. This kind of traversal is applied to all the
   subtrees in the tree. Here, we start by visiting the root node, then we go to its left child. If we find the left child is a root to other nodes,
   we visit it, then go to its left child also. We continue this until we find that the left child is the last one, then we visit it. After that, we visit the
   right child, then we go back up to visit the right child of the next root up. We do this recursively until the whole tree is traversed. Where we find a missing
   child, we skip that part.

   Pre-order traversal is used to create a copy of the tree. and is also used to get the prefix expression of an expression tree.

3. Post-order traversal (leftChild - rightChild - root)

   In post-order traversal, we start by visiting the left child, then we move to the right child and then the root node. We do this recursively until when we've
   visited every node in the tree. This traversal starts by looking for the leftmost node in the tree, then it visits that, then goes to its right sibling, then goes
   to the root. The root for each subtree is visited only when all the left and right children are visited in that order. If the visited root has a right sibling,
   we branch to that side and look for the leftmost child in that tree as well, then we go to its right sibling and back to the root. We go back up until the very
   topmost root is visited last.

   Post-order traversal is used to delete the tree and is also used to get the postfix expression of an expression tree.

## Application
Since a binary tree is hierarchical, it can be used to manipulate hierarchical data such as a file structure.

Binary trees can make information easy to search, e.g.
if we organized keys in a tree with some ordering like in a **Binary Search Tree**, we can search for a key in relatively moderate time.

We can insert or delete keys in a binary tree in a moderately quick time.

Binary trees can also be used in router algorithms.


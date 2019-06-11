# Depth Fist Search (DFS)
Depth-first search (DFS) is an algorithm for searching a graph or tree data structure.
The algorithm starts at the root (top) node of a tree and goes as far as it can down
a given branch (path), then backtracks until it finds an unexplored path, and then
explores it. The algorithm does this until the entire graph has been explored.

The implementation goes as follows;

Go to the specified start node. then, arbitrarily pick one of that node’s neighbors and go there.
If that node has neighbors, arbitrarily pick one of those and go there unless we’ve already seen that node.
We then repeat this process until one of two things happens. Either we reach the last node and we terminate
the algorithm or we reach a node with only neighbors that we’ve already seen,
or no neighbors at all, in which case, we go back one step and try one of the neighbors we didn’t try last time.

There are three different strategies for implementing DFS:
* Pre-order. This works by visiting the current node and successively moving to the left
until a leaf is reached, visiting each node on the way there. Once there are no more children
on the left of a node, the children on the right are visited.

* In-order. This finds the leftmost node in the tree, visits that node, and subsequently visits
the parent of that node. It then goes to the child on the right and finds the next leftmost node in the tree to visit.

* Post-order. This works by visiting the leftmost leaf in the tree, then it goes to the right sibling before going up to the parent
and down the second leftmost leaf in the same branch, and so on until the parent is the last node to be visited within a branch.

## Complexity
Depth-first search visits every vertex once and checks every edge in the graph once.
Therefore, DFS complexity is **O(V+E)** where **V** is number of vertices in the graph and **E** is
number of edges in the graph. This assumes that the graph is represented as an adjacency list.

## Application of Depth First Search
For an unweighted graph, DFS traversal of the graph produces the minimum spanning tree and all pair shortest path tree.

Detecting a cycle in a graph. A graph has cycle if and only if we see a back edge during DFS. So we can run DFS for the graph and check for back edges.

Solving puzzles with only one solution, such as mazes. DFS can be adapted to find all solutions to a maze by only including nodes on the current path in the visited set.

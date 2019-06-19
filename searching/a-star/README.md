# A* Search
A* Search algorithm is one of the best and popular techniques used in path-finding and graph traversals.
The algorithm efficiently plots a walkable path between multiple nodes, or points, on the graph.
The A* algorithm introduces a heuristic into a regular graph-searching algorithm, essentially planning ahead at each step so a more optimal decision is made.
A* works by making a lowest-cost path tree from the start node to the target node.

A* uses a function `f(n)` that gives an estimate of the total cost of a path using that node where;

    f(n) = g(n) + h(n)
where

* `f(n)` = total estimated cost of path through node *n*
* `g(n)` = cost so far to reach node *n*
* `h(n)` = estimated cost from *n* to goal. This is the heuristic part of the cost function, so it is like a guess.

A* algorithm begins at the start node, and considers all adjacent cells. Once the list of adjacent
cells has been populated, it filters out those which are inaccessible. It then picks the cell with the
lowest cost, that is, the one with the lowest estimated `f(n)`. This process is recursively repeated
until the shortest path has been found to the target. The computation of `h(n)` is done via a heuristic that usually gives good results.

There are generally three approximation heuristics used to calculate `h(n)`:
* Manhattan Distance. This is the sum of absolute values of differences in the goal’s x and y
coordinates and the current cell’s x and y coordinates respectively. We use this when we are allowed to move only in four directions only
(right, left, top, bottom).
    >h = abs(current_cell.x – goal.x) +
     abs(current_cell.y – goal.y)
* Diagonal Distance. This is the maximum of absolute values of differences in the goal’s x and y coordinates and the
current cell’s x and y coordinates respectively. This is used when we are allowed to move in eight directions only.
    >h = max { abs(current_cell.x – goal.x),
           abs(current_cell.y – goal.y) }
* Euclidean Distance. This is the distance between the current cell and the goal cell using this distance formula.
This is used when we are allowed to move in any direction.
    >h = sqrt((current_cell.x – goal.x)^2 +
            (current_cell.y – goal.y)^2)

## Limitations
A* Search Algorithm doesn’t produce the shortest path always, as it relies heavily on heuristics/approximations to calculate *h*

## Complexity
The worst case time complexity is **O(E)**, where **E** is the number of edges in the graph

## Application
A* is commonly used for the common pathfinding problem in applications such as games


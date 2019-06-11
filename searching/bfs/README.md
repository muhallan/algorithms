# Breadth First Search (BFS)
Breadth-first search starts by searching a start node, followed by its adjacent nodes,
then all nodes that can be reached by a path from the start node containing two edges, three edges, and so on.
The BFS algorithm visits all vertices in a graph that are *k* edges away from the source vertex *v*
before visiting any vertex *k+1* edges away. This is done until no more vertices are reachable from *v*.

In DFS, we explore all the neighbors of our starting node before exploring any other node.
After we have explored all the immediate neighbors we explore nodes that are 2 hops away
from the starting node. Then 3 hops, then 4 hops, and so on.
With BFS we’re not really exploring along a path, instead we’re exploring along several possible paths at once.
When one reaches a dead end, we just stop searching in that direction and focus on whatever
else is in the adjacent direction. If the graph is unweighted BFS will always find the shortest path.

In BFS, you traverse the graph breadthwise by first moving horizontally and visiting all the nodes of the current layer
and then moving to the next layer.

## Complexity
The time complexity of BFS is **O(V + E)**, where **V** is the number of vertices and **E** is the number of edges in the graph.

## Application of Depth First Search
Shortest Path and Minimum Spanning Tree for unweighted graphs. In an unweighted graph, the shortest path is
the path with least number of edges. With Breadth First Search, we always reach a vertex from given source
using the minimum number of edges. Also, in case of unweighted graphs, any spanning tree is
Minimum Spanning Tree and we can use either BFS for finding a spanning tree.

Peer to Peer Networks. In Peer to Peer Networks like BitTorrent, Breadth First Search is used to find all neighbor nodes.

Social Networking Websites. In social networks, we can find people within a given distance 'k'
from a person using Breadth First Search till 'k' levels.
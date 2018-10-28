# Graphs
A graph is a data structure that represents sets of objects where some pairs of objects are
connected by links. The interconnected objects are represented by points called `vertices` and the
links that connect the `vertices` are called `edges`. An edge connects two vertices to show that
there is a relationship between them. Edges may be one-way or two-way. If the edges in a graph are
all one-way, that graph is a `directed graph` or a `digraph`. Edges may contain a `weight` that
indicates the cost to go from one vertex to another. A `path` in a graph is a sequence of vertices
that are connected by edges. A `cycle` in a directed graph is a path that starts and ends at the same
vertex. A graph with no cycles is called an `acyclic graph`. A directed graph with no cycles is called a
`directed acyclic graph (DAG)`.

A graph is commonly represented as an `adjacency matrix` and an `adjacency list`.

1. Adjacency Matrix

   This uses a two-dimensional matrix to represent a graph. In this representation, each of the rows
   and columns represent a vertex in the graph. If it's a weighted graph, the value that is stored in
   the cell which is the intersection of row v and column w indicates the weight of the edge from vertex
   v to vertex w. For non-weighted graphs, presence of a vertex can be shown by filling the intersection cell
   of a row and column by 1 and leaving the rest as 0.

   The adjacency matrix can be represented as a 2D array of size V * V where V is the number of vertices in
   the graph.

   The advantage of an adjacency matrix is that it is simple to implement and follow. For smaller graphs, it
   is easy to see which nodes are connected to other nodes.

   Its disadvantage is that it consumes a lot of space which is **O(V^2)**. Even when the graph has few edges
   (sparse), it still consumes the same space.
1. Adjacency List

   In this implementation, a graph is represented as a dictionary of vertices where the key of each vertex is its name
   and the value is the list of other vertices that it's connected to. In case it's a weighted graph, the vertices can be
   represented as a pair, making it a list of pairs or a list of dictionaries in Python where the keys are the
   vertices and the values are the weights. The example code uses an adjacency list.

   The size of the dictionary is equal to the number of the vertices in the graph.

   The advantage of an adjacency list is that it saves space, and it compactly represents a sparse graph.
   We can also easily find all the links that are directly connected to a particular vertex.


## Applications
Social network graphs. Graphs are used to represent relationships between users in social network sites
like Facebook, Twitter, Instagram or LinkedIn. They are used to show users that are communicating with each other,
those that influence each other or even if users know each other.

Maps applications. Graphs are used by apps such as Google Maps, Bing maps to find the shortest routes between
locations or getting to know traffic patterns. Intersections of roads are considered as vertices and the roads
connecting the vertices are the edges.

In computer science, graphs are used to solve a number of problems by representing flow of
information.


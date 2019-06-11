from collections import defaultdict


class Graph:
    """
    This class represents a directed graph using adjacency list representation
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, neighbor):
        """
        Adds an edge to the graph
        :param vertex: The value of a vertex to be added
        :param neighbor: The value of a neighboring node to the vertex
        """
        self.graph[vertex].append(neighbor)

    def dfs_helper(self, vertex, visited):
        """
        A Depth First Search helper method to print and mark a node as visited
        :param vertex: The node to be visited
        :param visited: A list containing nodes that have been visited
        """
        # mark the node as visited
        visited[vertex] = True
        print(vertex)

        # visit all the neighboring vertices
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited)

    def dfs(self, root_vertex):
        """
        The function to carry out the depth first search
        :param root_vertex: The node to start the traversal from
        """
        # initialize all nodes to not visited
        visited = [False]*len(self.graph)

        # create an empty queue
        queue = []

        # mark the starting node as visited and enqueue it
        queue.append(root_vertex)
        visited[root_vertex] = True

        while queue:
            # dequeue a node print it
            vertex = queue.pop(0)
            print(vertex)

            # visit all the neighboring vertices of the dequeued vertex while
            # visiting the unvisited ones and marking them as visited and
            # enqueueing them
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Search starting from vertex 2")
g.dfs(2)

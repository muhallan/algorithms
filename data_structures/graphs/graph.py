class Vertex:
    """
    This class represents each vertex in the graph.
    Each vertex uses a dictionary to keep track of the vertices to which it is
    connected to, and the weight of each edge
    """
    def __init__(self, key):
        """
        Initialize a vertex with a given id which is the key by which it is
        referred.
        :param key: string. The name of the vertex
        """
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        """
        Used to add a connection from this vertex to another vertex
        represented by neighbor.
        :param neighbor: Vertex. The neighboring vertex to connect to
        :param weight: int. The weight of the vertex to connect to
        """
        self.connected_to[neighbor] = weight

    def get_connections(self):
        """
        Returns all the vertices this vertex is connected to
        :return: list. List of the connected vertices as represented by the
        connected_to instance variable
        """
        return self.connected_to.keys()

    def get_id(self):
        """
        Get the id of the vertex
        :return: str. The id of the vertex
        """
        return self.id

    def get_weight(self, neighbor):
        """
        Get the weight of the given neighboring vertex
        :param neighbor: Vertex. The neighboring vertex whose weight is required
        :return: int. The weight of the provided neighbor
        """
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.id) + ' connected_to: ' + str([x.id for x in self.connected_to])


class Graph:
    """
    This class represents the whole graph. It holds the dictionary of vertices
    that maps vertex names to vertex objects
    """
    def __init__(self):
        self.vertex_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        """
        Add a new vertex to the graph
        :param key: str. The name of the vertex to be added
        :return: Vertex. The newly created vertex object
        """
        self.num_of_vertices = self.num_of_vertices + 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """
        Get the Vertex represented by the given key
        :param key: str. The name of the vertex to return
        :return: Vertex. Get the vertex object represented by the given key
        if it's available, else return None
        """
        return self.vertex_list[key] if key in self.vertex_list else None

    def add_edge(self, vertex_key_one, vertex_key_two, weight=0):
        """
        Add a connection/edge between two vertices whose keys are supplied
        and give it the weight provided
        :param vertex_key_one: str. The key of vertex to add an edge to
        :param vertex_key_two: str. The key of the vertex to connect to
        :param weight: int. The weight to give to the edge
        """
        if vertex_key_one not in self.vertex_list:
            self.add_vertex(vertex_key_one)
        if vertex_key_two not in self.vertex_list:
            self.add_vertex(vertex_key_two)
        self.vertex_list[vertex_key_one].add_neighbor(self.vertex_list[vertex_key_two], weight)

    def get_vertices(self):
        """
        Get all the vertices in the graph
        :return: list. The list of all the keys of the vertices in the graph
        """
        return list(self.vertex_list.keys())

    def __contains__(self, key):
        return key in self.vertex_list

    def __iter__(self):
        return iter(self.vertex_list.values())


# testing
graph = Graph()
for i in range(6):
    graph.add_vertex(i)

graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 4)
graph.add_edge(2, 3, 9)
graph.add_edge(3, 4, 7)
graph.add_edge(3, 5, 3)
graph.add_edge(4, 0, 1)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 1)

# vertices in the graph
print(graph.get_vertices())

# number of vertices
print(graph.num_of_vertices)

# each vertex
for vertex in graph:
    print(vertex)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return None

    def __str__(self):
        res = ""
        for vertex in self.graph:
            res += str(vertex) + " -> " + str(self.graph[vertex]) + "\n"
        return res

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex("Amravati")
    graph.add_vertex("Jalgaon")
    graph.add_vertex("Chandrapur")
    graph.add_vertex("Pune")
    graph.add_vertex("Ahmadnagar")

    graph.add_edge("Amravati", "Jalgaon")
    graph.add_edge("Amravati", "Chandrapur")
    graph.add_edge("Jalgaon", "Pune")
    graph.add_edge("Pune", "Ahmadnagar")
    graph.add_edge("Chandrapur", "Ahmadnagar")
    graph.add_edge("Ahmadnagar", "Amravati")

    print(graph)
    graph.remove_vertex("Pune")
    graph.remove_edge("Jalgaon", "Pune")


    print(graph)
    print("Neighbours:", graph.get_neighbors("Amravati"))
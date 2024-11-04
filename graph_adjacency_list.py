class Graph:
    # Initialize an empty graph in form of a dictionary
    def __init__(self):
        self.graph = {}
    
    # Method to add node to a graph
    def add_node(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = self.graph[v]
    
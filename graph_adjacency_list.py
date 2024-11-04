class Graph:
    # Initialize an empty graph in form of a dictionary
    def __init__(self):
        self.graph = {}
    
    # Method to add node to a graph
    def add_node(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    # method to display the graph
    def display_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Instantiate the the graph object
graph = Graph()


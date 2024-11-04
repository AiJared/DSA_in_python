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

# Add nodes to the graph
graph.add_node(0, 1)
graph.add_node(0, 2)
graph.add_node(1, 2)
graph.add_node(2, 0)
graph.add_node(2, 3)

# Display the graph
print("Graph Adjacency List: ")
graph.display_graph()
class Node:
    """
    An object for storing a single object of a linked list
    Models two attributes - daa and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
# implementing the node
N1 = Node(10)
print(N1)
N2 = Node(20)
print(N2)
N1.next_node = N2
print(N1.next_node)
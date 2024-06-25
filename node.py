class Node:
    """
    A node stores data and a reference to the next node in a linked list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    

# Implementing the node
n1 = Node(10)
print(n1)
n2 = Node(12)
print(n2)
# next node
n1.next_node = n2
print(n1.next_node)
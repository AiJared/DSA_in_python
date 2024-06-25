# Creating the node
class Node:
    """
    A node stores the data item and a reference to the next node
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    

# Create a Singly Linked List

class SinglyLinkedList(Node):
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        A function to check if the list is empty
        """
        return self.head == None
    
    def size(self):
        """
        A function to calculate the size of the list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
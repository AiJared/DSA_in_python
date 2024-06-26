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
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        A function to search for the first node containing the data that matches the key in a linked list
        It returns the node or none if the node is not found.
        It runs in linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            
            return current.next_node
        
        return None

# create a singly linked list
lst = SinglyLinkedList()
n1 = Node(1)
lst.head = n1

#print the size of the list
print(lst.size())

# add elements to the list
lst.add(12)
lst.add(21)
lst.add(76)

print(lst.size())
# Create the node
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # referencing to the next node
        self.next = next
        # referencing to the previous node
        self.prev = prev
        self.data = data

def traverse(head):
    """
    Traverse through the list as you print its elements
    """
    current = head
    while current:
        # Print current node's data
        print(current.data, end=" <-> ")
        # Go to the next node
        current = current.next
    # Print None if the list is empty
    print("None")

def insert_at_the_beginning(head, data):
    """
    Inserting new data at the beginnig of the list
    """
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Create the list    
head = None
head = insert_at_the_beginning(head, 4)
head = insert_at_the_beginning(head, 3)
head = insert_at_the_beginning(head, 2)
head = insert_at_the_beginning(head, 1)

# traverse and print the nodes
traverse(head)
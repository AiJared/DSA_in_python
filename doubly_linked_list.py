# Create the node
class Node:
    def __init__(self, data):
        # referencing to the next node
        self.next = None
        # referencing to the previous node
        self.prev = None
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

# Show the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Create the list    
head = None
head = insert_at_the_beginning(head, 3)
head = insert_at_the_beginning(head, 2)
head = insert_at_the_beginning(head, 1)

# traverse and print the nodes
traverse(head)

print("Doubly Linked List after insertion at the beginning: ")
display(head)
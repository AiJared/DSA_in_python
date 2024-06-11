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

def insert_before_node(node, data):
    """
    Insert a node before a given node in the list
    """
    if node is None:
        print("Error: The given node is None")
        return
    
    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node

    if node.prev:
        node.prev.next = new_node
    
    node.prev = new_node


def insert_after_node(node, data):
    """
    Insert a node after a given node
    """
    if node is None:
        print("Error: The given node is None")
        return
    
    new_node = Node(data)
    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node

# Show the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Create the list    
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

# traverse and print the nodes
traverse(head)

print("Doubly Linked List before insertion:")
display(head)

insert_before_node(node2, 4)

print("Doubly Linked List after insertion: ")
display(head)
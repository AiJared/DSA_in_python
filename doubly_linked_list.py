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

def insert_at_end(head, data):
    """
    Insert a new node at the end of the list
    """
    new_node = Node(data)
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head

def delete_at_beginning(head):
    """
    Delete the first node of the list, which basically is the head of the list
    """
    if head is None:
        print("Doubly linked list is empty")
        return None
    
    if head.next is None:
        return None
    
    new_head = head.next
    new_head.prev = None
    del head
    return new_head

def delete_at_position(head, position):
    """
    Delete the node at a given position from the doubly linked list
    """
    if head is None:
        print("Doubly linked is empty")
        return None
    
    if position < 0:
        print("Invalid position")
        return head
    
    if position == 0:
        if head.next:
            head.next.prev = None
        return head.next
    
    current = head
    count = 0
    while current and count < position:
        current = current.next
        count += 1

    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
    
    del current
    return head

# Show the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Create the list    

head = None
head = insert_at_the_beginning(head, 4)
head = insert_at_the_beginning(head, 3)
head = insert_at_the_beginning(head, 2)
head = insert_at_the_beginning(head, 1)

# Delete the first node
head = delete_at_position(head, 2)

# Traverse and print the nodes after deletion
traverse(head)
# Representing a circular linked list in Python
class Node:
    def __init__(self, data):
        # Data stored in the node
        self.data = data
        # reference to the next node in the circular linked list
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with head
        # pointer poiniting to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the
        # circular linked list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                # Traverse the list until the last node
                current = current.next
            # Make the last node point to the new node
            current.next = new_node
            # Make the new node point back to the head
            new_node.next = self.head

    def insert_at_beginning(self, data):
        # Insert a new node with data at the beginnig of the
        # linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            # Traverse through each node and print is
            # its data
            print(current.data, end=" -> ")
            current = current.next
        # Print None to indicate the end of the linked list
        print(None)
    
    def traverse(self):
        # Traverse and display the elements of the circular linked list
        if not self.head:
            print("Circular Linked list is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                # Break the loop when we reach the head again
                break

# Driver code
circular_linked_list = CircularLinkedList()
circular_linked_list.insert_at_beginning(3)
circular_linked_list.insert_at_beginning(2)
circular_linked_list.insert_at_beginning(1)

print("Linked List after inserting at the beginning:")
circular_linked_list.display()
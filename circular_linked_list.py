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

    def insert_at_position(self, position, data):
        # Insert a new node with data at the specified
        # position in the linked list
        new_node = Node(data)
        # check if the position is valid
        if position < 0:
            print("Invalid position")
            return
        # If the position is 0, insert the new node at the beginning
        # of the linked list
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        # Traverse the list until the node before the specified position
        while count < position - 1 and current:
            current = current.next
            count += 1
        # If the position is out of range, print an error message
        if not current:
            print("Position out of range")
            return
        # Insert the new node at the specified position
        new_node.next = current.next
        current.next = new_node
        

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
circular_linked_list.insert_at_position(0, 1)
circular_linked_list.insert_at_position(1, 3)
circular_linked_list.insert_at_position(1, 2)

print("Linked List after inserting at a position:")
circular_linked_list.display()
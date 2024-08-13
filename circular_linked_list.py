# Representing a circular linked list in Python
class Node:
    def __init__(self, data):
        # Data stored in the node
        self.data = data
        # reference to the next and previous node in the circular linked list
        self.next = None
        self.pre = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with head
        # pointer poiniting to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the linked list
        new_node = Node(data)
        if not self.head:
            # If the linked list is empty, make the new node the head
            self.head = new_node
            return
        current = self.head
        while current.next:

            # Traverse the linked list until the last node
            current = current.next

        # Assign the new node as the next node of the last node
        current.next = new_node

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
        
    def delete_at_beginning(self):
        if not self.head:
            print("Circular Linked List is empty")
            return

        # If there is only one node in the list
        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
            
        # Update the last node to point to the second node
        current.next = self.head.next
        
        # Update the head to point to the second node
        self.head = self.head.next

    def delete_at_position(self, position):
        if not self.head:
            print("Circular Linked List is empty")
            return
        if position < 0:
            print("Invalid position")

        # Delete the head node
        if position == 0:
            # Only one node in the list
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        count = 0
        while count < position -1 and current.next != self.head:
            current = current.next
            count += 1
        if count < position - 1:
            print("Position out of range")
            return
        current.next = current.next.next

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
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)

print("Circular Linked List before deletion:")
circular_linked_list.display()
print()

circular_linked_list.delete_at_position(1)

print("Circular Linked List after deletion at position1: ")
circular_linked_list.display()
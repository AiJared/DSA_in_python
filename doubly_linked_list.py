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
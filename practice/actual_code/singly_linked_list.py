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
    
    # Size of the list
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
            
            else:
                current = current.next_node
        
        return None
    
    def insert(self, data, index):
        """
        Inserts new Node containing data at index position.
        Insertion takes O(1) but finding the node at the insertion
        point takes O(n) time. So it takes overall O(n) time.
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes the node containing data that matches the key
        and returns the node or none if the key doesn't have a match
        Takes linear time.
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes linear time.
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return "->".join(nodes)
    

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

lst.add(10)
lst.add(22)
lst.add(45)
lst.add(23)

n = lst.search(45)
print(n)
l = lst.search(11)
print(l)

print(lst.size())
# lst.insert(5, 27)
print(lst.size())
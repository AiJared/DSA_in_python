class Node:
    """
    An object for storing a single object of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
# implementing the node
N1 = Node(10)
print(N1)
N2 = Node(20)
print(N2)
N1.next_node = N2
print(N1.next_node)

"""
Nodes are the building blocks for a list. And now that we have a node,
we are going to use it to create a singly linked list.
"""

class LinkedList(Node):
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    """
    Ideally we would try not to expose the inner workings of our data structure
    to the code that uses it. Instead let's make this operation expression explicity
    by defining a method.
    """
    def is_empty(self):
        return self.head == None
    """
    All we doing here is checking to see if head is None. If it is then the return
    gives us True which evaluates that the list is empty.

    Let's add one more convinience method to calculate the size of our list. The name
    convinience method indicates that what this method is doing is not providing any
    additional functionality that our data structure can't handle right now but instead
    making existing functionality easier to use.

    We could calculate the size of our linked list by traversing it everytime using a loop
    until we hit a tail node but doing that everytime is a husle.  
    """
    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time.
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count
    def add(self, data):
        """
        Adds new Node containing data at the head of the list
        Takes O(1) time.
        """
        new_node = Node(data) 
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time
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
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        Therefore it takes an overall O(n) time.
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
        Removes Node containing data that matches the key
        Returns the node or None if the key doen't exist
        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
        
            current = current.next_node
        return '->'.join(nodes)

l = LinkedList()
N1 = Node(10)
l.head = N1
print(l.size())

# inserting values to a linked list
"""
Since our list only keeps a reference to the head 
we are going to add a new item to the head of the list.
"""
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
print(l)
l.add(10)
l.add(2)
l.add(45)
l.add(15)

n = l.search(45)
print(n)
print(l)
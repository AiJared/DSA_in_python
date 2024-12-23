class Node:
    # constructor method initializing left and right nodes and value
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Insert nodes in a binary tree
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    
    return root

# In order traversal (left, root, right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end="")
        inorder_traversal(root.right)

# Example usage
root = Node(10)
insert(root, 5)
insert(root, 15)
insert(root, 2)
insert(root, 7)

print("In-order traversal:")
inorder_traversal(root)

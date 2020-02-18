class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insertion(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def insertion(self, node, val):
        if node.value < val:
            if node.right:
                return self.insertion(node.right, val)
            else:
                node.right = Node(val)
        else:
            if node.left:
                return self.insertion(node.left, val)
            else:
                node.left = Node(val)

    def search_helper(self, node, val):
        if node.value == val:
            return True
        else:
            if node.right:
                return self.search_helper(node.right, val)
            if node.left:
                return self.search_helper(node.left, val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
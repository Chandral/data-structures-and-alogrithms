class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current_parent_node = self.root
        while True:
            if current_parent_node.value > new_val:
                if current_parent_node.left:
                    current_parent_node = current_parent_node.left
                else:
                    current_parent_node.left = Node(new_val)
                    break
            elif current_parent_node.value < new_val:
                if current_parent_node.right:
                    current_parent_node = current_parent_node.right
                else:
                    current_parent_node.right = Node(new_val)
                    break

    def search(self, find_val):
        current_parent_node = self.root
        while True:
            if current_parent_node.value == find_val:
                return True
            else:
                if current_parent_node.value > find_val:
                    if current_parent_node.left:
                        current_parent_node = current_parent_node.left
                    else:
                        return False
                elif current_parent_node.value < find_val:
                    if current_parent_node.right:
                        current_parent_node = current_parent_node.right
                    else:
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

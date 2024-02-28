class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current_node = self.root
        while True:
            if value >= current_node.value:
                if not current_node.right:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right
            else:
                if not current_node.left:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left

    def lookup(self, value):
        if not self.root:
            return

        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node

            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return

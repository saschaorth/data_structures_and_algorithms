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

    def _reconnect(self, value, parent_node=None, child_node=None):
        if not parent_node:
            self.root = child_node
        elif parent_node.value > value:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

    def remove(self, value):
        if not self.root:
            return

        current_node = self.root
        parent_node = None
        while current_node:
            if value == current_node.value:
                if not current_node.right and not current_node.left:  # no children
                    self._reconnect(value, parent_node)
                elif not current_node.right:  # only left child
                    self._reconnect(value, parent_node, current_node.left)
                elif current_node.right.left:  # right child has left child
                    to_delete_node = current_node.right.left
                    self.remove(to_delete_node.value)  # remove the left child of the right child
                    to_delete_node.left = current_node.left
                    to_delete_node.right = current_node.right
                    self._reconnect(value, parent_node, to_delete_node)
                else:  # only right child
                    current_node.right.left = current_node.left
                    self._reconnect(value, parent_node, current_node.right)
                break

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                parent_node = current_node
                current_node = current_node.left
        return


# visualize tree with
def traverse(node):
    if node is None:
        return None

    tree = dict(value=node.value)
    tree["left"] = traverse(node.left)
    tree["right"] = traverse(node.right)

    return tree

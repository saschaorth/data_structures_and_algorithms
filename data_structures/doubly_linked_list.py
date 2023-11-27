class Node():
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        new_node.previous = None
        self.head = new_node
        self.length += 1

    def __repr__(self):
        linked_list = []
        current_node = self.head
        while current_node:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return str(linked_list)
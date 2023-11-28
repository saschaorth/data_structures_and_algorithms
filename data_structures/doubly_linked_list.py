class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
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

    def get_node(self, index, start_from="head"):
        if start_from not in ["head", "tail"]:
            raise Exception("start_from must be head or tail")
        current_node = getattr(self, start_from)
        counter = 0

        while counter < index:
            if start_from == "head":
                current_node = current_node.next
            else:
                current_node = current_node.previous
            counter += 1
        return current_node

    def insert(self, index, value):
        if (index + 1) > self.length:
            self.append(value)
            return

        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        if (index + 1) > (self.length / 2):
            leading_node = self.get_node(self.length - index, start_from="tail")
        else:
            leading_node = self.get_node(index - 1)
        following_node = leading_node.next
        new_node.next = following_node
        leading_node.next = new_node
        self.length += 1

    def is_tail(self, index):
        return (index+1) >= self.length

    def ensure_index_within_range(self, index):
        if (index+1) > self.length:
            index = (self.length-1)
        return index

    def update_tail(self, node):
        current_node = node
        while current_node:
            self.tail = current_node
            current_node = current_node.next

    def remove(self, index):
        if self.length == 1:
            raise ValueError('You can not remove the only Node')
        index = self.ensure_index_within_range(index)

        if (index + 1) > (self.length / 2):
            leading_node = self.get_node(self.length - index, start_from="tail")
        else:
            leading_node = self.get_node(index - 1)
        to_remove_node = leading_node.next
        following_node = to_remove_node.next

        if index == 0:
            self.head = following_node
        else:
            leading_node.next = following_node

        if self.is_tail(index):
            self.update_tail(leading_node)
        self.length -= 1

    def __repr__(self):
        linked_list = []
        current_node = self.head
        while current_node:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return str(linked_list)

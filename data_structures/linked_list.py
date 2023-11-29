class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(
            {
                'value': self.value,
                'next': self.next
            }
        )


class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def get_node(self, index):
        current_node = self.head
        counter = 0

        while counter < index:
            current_node = current_node.next
            counter += 1
        return current_node

    def insert(self, index, value):
        if (index+1) > self.length:
            self.append(value)
            return

        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        leading_node = self.get_node(index-1)
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

        leading_node = self.get_node(index-1)
        to_remove_node = leading_node.next
        following_node = to_remove_node.next

        if index == 0:
            self.head = following_node
        else:
            leading_node.next = following_node

        if self.is_tail(index):
            self.update_tail(leading_node)
        self.length -= 1

    def reverse(self):
        current_node = self.head
        leading_node = None
        while current_node:
            following_node = current_node.next
            current_node.next = leading_node
            leading_node = current_node
            current_node = following_node
        self.head = leading_node

    def __repr__(self):
        linked_list = []
        current_node = self.head
        while current_node:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return str(linked_list)
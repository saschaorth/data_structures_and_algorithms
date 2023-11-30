class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    top = None
    bottom = None
    length = 0

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if not self.bottom:
            return
        new_top = self.top.next
        self.top = new_top
        self.length -= 1
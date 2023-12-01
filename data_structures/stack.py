class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
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
        if self.length == 1:
            self.bottom = None
        if not self.bottom:
            return
        new_top = self.top.next
        self.top = new_top
        self.length -= 1


class ListStack:
    top = None
    bottom = None
    length = 0

    def peek(self):
        return self.top[-1]

    def push(self, value):
        if self.length == 0:
            self.top = [value]
            self.bottom = [value]
        else:
            self.top.append(value)
        self.length += 1

    def pop(self):
        if self.length == 1:
            self.bottom = None
        self.top.pop()
        self.length -= 1
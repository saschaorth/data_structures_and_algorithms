class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    top = None
    length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        new_top = self.top.next
        self.top = new_top
        self.length -= 1


class ListStack:
    lst = []

    def peek(self):
        return self.lst[-1]

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        if not self.lst:
            return
        self.lst.pop()

class LinkedList():
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {'value': value, 'next': None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = {'value': value, 'next': None}
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1

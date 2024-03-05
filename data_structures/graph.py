class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_node(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, from_node, to_node):
        self.adjacent_list[from_node].append(to_node)
        self.adjacent_list[to_node].append(from_node)

    def show_connections(self):
        all_nodes = list(self.adjacent_list.keys())
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = " ".join(node_connections)
            print(node + "-->" + connections)
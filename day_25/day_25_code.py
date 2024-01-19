import networkx as nx


class GraphSeparation:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = nx.Graph()
        self.answer = 0

    def start(self):
        self.iterate()
        self.cut()

        return self.answer

    def iterate(self):
        graph = nx.Graph()
        for line in self.input:
            line = line.strip()
            line = line.split(': ')
            key, components = line[0], line[1].split()

            for val in components:
                graph.add_edge(key, val)
                graph.add_edge(val, key)

        self.data = graph

    def cut(self):
        data = self.data

        split = nx.minimum_edge_cut(data)
        data.remove_edges_from(split)
        x, y = nx.connected_components(data)

        self.answer = len(x) * len(y)

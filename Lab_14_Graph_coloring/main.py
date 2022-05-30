class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for i in range(vertex)] for i in range(vertex)]
        self.connections = {}

    def graph_init(self, list_of_edges):
        for index in range(self.V):
            index_connected = []
            for subindex in range(self.V):
                if list_of_edges[index][subindex] != 0:
                    index_connected.append(subindex)
                    self.graph[index][subindex] = 1
                    self.graph[subindex][index] = 1
            self.connections.update({index: index_connected})
        return self.graph

    def output(self):
        _tuple = sorted(self.colorNodes().items(), key=lambda x: x[1])
        for index in range(len(_tuple)):
            print(f'{_tuple[index][0]} - {_tuple[index][1]}')

    def colorNodes(self):
        color_map = dict()
        # проверяем вершины по убыванию количества соседей
        for node in sorted(self.connections, key=lambda x: len(self.connections[x]), reverse=True):
            # находим цвета соседей
            neighbor_сolors = set(color_map.get(neigh)
                                  for neigh in self.connections[node])
            color_map[node] = [color for color in range(
                len(self.connections)) if color not in neighbor_сolors][0]
            # берем все возможные цвета убираем из них те которые у соседей и берем первый из оставшихся
        return color_map


test_graph = [
    [0, 1, 0, 0, 0, 0, 1],  # 0
    [1, 0, 1, 0, 0, 1, 1],  # 1
    [0, 1, 0, 1, 1, 1, 0],  # 2
    [0, 0, 1, 0, 1, 0, 0],  # 3
    [0, 0, 1, 1, 0, 1, 1],  # 4
    [0, 1, 1, 0, 1, 0, 1],  # 5
    [1, 1, 0, 0, 1, 1, 0],  # 6
]
test_graph_2 = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]
test = Graph(7)
test.graph_init(test_graph)
test.output()

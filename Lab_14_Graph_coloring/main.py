class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for i in range(vertex)] for i in range(vertex)]
        self.connections = {}

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


def graph_init(graph, list_of_edges):
    for index in range(graph.V):
        index_connected = []
        for subindex in range(graph.V):
            if list_of_edges[index][subindex] != 0:
                index_connected.append(subindex)
                graph.graph[index][subindex] = 1
                graph.graph[subindex][index] = 1
        graph.connections.update({index: index_connected})
    return graph


test_graph = [
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0],
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
my_graph = Graph(10)
my_graph = graph_init(my_graph, test_graph_2)


def output(graph):
    _tuple = sorted(graph.colorNodes().items(), key=lambda x: x[1])
    for index in range(len(_tuple)):
        print(f'{_tuple[index][0]} - {_tuple[index][1]}')


output(my_graph)

# Алгоритм Прима поиска минимального остова графа
import math
# список ребер графа (длина, вершина 1, вершина 2)
# первое значение возвращается, если нет минимальных ребер
R = [(math.inf, -1, -1), (13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]


class Graph:
    def __init__(self, vertices, vertex_count=6):
        self.vertices = vertices
        self.vertex_count = vertex_count
        self.connected = {1}
        self.verges = list()

    def get_min(self):
        _min = (math.inf, -1, -1)
        for vertex in self.connected:
            current_min = min(self.vertices, key=lambda x: x[0] if (x[1] == vertex or x[2] == vertex) and (
                x[1] not in self.connected or x[2] not in self.connected) else math.inf)
            if _min[0] > current_min[0]:
                _min = current_min

        return _min

    def algorythm_prima(self):
        while len(self.connected) < self.vertex_count:
            # ребро с минимальным весом
            _min = self.get_min()
            if _min[0] == math.inf:    # если ребер нет, то остов построен
                break

            self.verges.append(_min)
            self.connected.add(_min[1])
            self.connected.add(_min[2])
        return self.verges


test = Graph(R)
print(test.get_min())
print(f'Результат работы алгоритма Прима:\n{test.algorythm_prima()}')

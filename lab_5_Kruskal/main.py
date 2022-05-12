# список ребер графа (длина, вершина 1, вершина 2)
R = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]


class Graph:
    def __init__(self, vertices):
        self.vertices = sorted(vertices)
        self.connected_vertices = set()
        self.isolated = {}
        self.verges = []  # verge = ребро

    def create_isolated_groups(self):
        for vertex in self.vertices:
            # проверка для исключения циклов в остове
            if vertex[1] not in self.connected_vertices or vertex[2] not in self.connected_vertices:
                if vertex[1] not in self.connected_vertices and vertex[2] not in self.connected_vertices:
                    # формируем в словаре ключ с номерами вершин
                    self.isolated[vertex[1]] = [vertex[1], vertex[2]]
                    # и связываем их с одним и тем же списком вершин
                    self.isolated[vertex[2]] = self.isolated[vertex[1]]
                else:
                    if not self.isolated.get(vertex[1]):
                        self.isolated[vertex[2]].append(vertex[1])
                        self.isolated[vertex[1]] = self.isolated[vertex[2]]
                    else:
                        self.isolated[vertex[1]].append(vertex[2])
                        self.isolated[vertex[2]] = self.isolated[vertex[1]]

                self.verges.append(vertex)
                self.connected_vertices.add(vertex[1])
                self.connected_vertices.add(vertex[2])

    def connect_groups(self):
        for vertex in self.vertices:
            # если вершины принадлежат разным группам, то объединяем
            if vertex[2] not in self.isolated[vertex[1]]:
                self.verges.append(vertex)
                gr1 = self.isolated[vertex[1]]
                self.isolated[vertex[1]] += self.isolated[vertex[2]]
                self.isolated[vertex[2]] += gr1

    def Kruskal(self):
        self.create_isolated_groups()
        self.connect_groups()
        return self.verges


test = Graph(R)
print(f'Результат работы алгоритма Крускала:\n{test.Kruskal()}')

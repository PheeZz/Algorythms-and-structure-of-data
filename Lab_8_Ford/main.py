
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices  # количество вершин
        self.graph = []  # словарь ребер

    def addEdge(self, start, end, weight):
        self.graph.append([start, end, weight])

    def output(self, dist):
        print("Список кратчайщих расстояний от источника:")
        for i in range(self.vertices):
            print(f'{i}\t{dist[i]}')

    def BellmanFord(self, source):
        '''
        инициализация массива расстояний от источника до всех вершин
        (с расстоянием принимаемым равным бесконечности),
        кроме расстояния от источника до самого источника
        '''
        dist = [float("Inf")] * self.vertices
        dist[source] = 0

        '''
        вычисляем самые короткие расстояния от источника до всех вершин
        len(vertices) - 1 раз по всем вершинам
        '''
        for _ in range(self.vertices - 1):
            for start, end, weight in self.graph:
                if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                    dist[end] = dist[start] + weight

        '''
        проверка на цикл отрицательноого веса
        Если мы снова переберем все ребра и получим более короткий путь для любой из вершин,
        это будет сигналом присутствия цикла отрицательного веса.
        '''
        for start, end, weight in self.graph:
            if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.output(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFord(0)

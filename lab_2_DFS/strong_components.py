'''
4. Найти в заданном орграфе количество и состав сильно связных
компонент с помощью поиска в глубину.
'''

from collections import defaultdict


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        # можно использовать генератор для заполнения значений по умолчанию, но так проще
        self.graph = defaultdict(list)

    def add_edge(self, _from, to):
        self.graph[_from].append(to)

    def dfs(self, point, visited_vertex):
        visited_vertex[point] = True
        print(point, end='')
        for i in self.graph[point]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, point, visited_vertex, stack):
        visited_vertex[point] = True
        for i in self.graph[point]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(point)

    # переворачиваем граф, для поиска компонент связности в обратном порядке
    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # выводим компоненты сильной связности
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()
        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print('')


test_graph = Graph(9)
test_graph.add_edge(0, 1)
test_graph.add_edge(0, 2)
test_graph.add_edge(1, 3)
test_graph.add_edge(1, 4)
test_graph.add_edge(2, 0)
test_graph.add_edge(4, 1)
test_graph.add_edge(3, 4)
test_graph.add_edge(3, 5)
test_graph.add_edge(4, 5)
test_graph.add_edge(5, 4)
test_graph.add_edge(5, 0)
test_graph.add_edge(5, 7)
test_graph.add_edge(7, 6)
test_graph.add_edge(6, 7)
test_graph.add_edge(7, 8)
test_graph.add_edge(8, 7)
test_graph.add_edge(8, 6)

print("Сильно связанные компоненты:")
test_graph.print_scc()

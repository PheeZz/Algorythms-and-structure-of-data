def find_eulerian_path(graph):
    path = []  # путь эйлера
    stack = []
    stack.append(graph[0][0])

    while len(stack) > 0:
        vertex = stack[len(stack) - 1]
        degree = get_degree(vertex, graph)

        if degree == 0:
            stack.pop()
            path.append(vertex)
        else:
            index, edge = get_edge_and_index(vertex, graph)
            graph.pop(index)
            stack.append(edge[1] if vertex == edge[0] else edge[0])
    return path


def get_degree(vertex, graph):
    '''
    в момент когда попадаем в тупик, не пройдя все ребра из вершины,
    откатываемся назад и проверяем вершину на наличие непройденных ребер
    '''
    degree = 0
    for (start, end) in graph:
        if vertex == start or vertex == end:
            degree += 1

    return degree


def get_edge_and_index(vertex, graph):
    '''
    получение индекса ребра и его значения после отката из тупика
    '''
    for i in range(len(graph)):
        if (vertex == graph[i][0] or vertex == graph[i][1]):
            edge, index = graph[i], i
            break

    return index, edge


graph = [
    (0, 1), (1, 5), (1, 7), (4, 5),
    (4, 8), (1, 6), (3, 7), (5, 9),
    (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)
]

print(f'Путь эйлера:\n{find_eulerian_path(graph)}')

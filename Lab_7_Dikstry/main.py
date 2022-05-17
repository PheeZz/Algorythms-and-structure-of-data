import math


def arg_min(last_str, watched):
    _min = -1
    _max = math.inf  # максимальное значение
    for index, value in enumerate(last_str):
        if value < _max and index not in watched:
            _max = value
            _min = index

    return _min


graph = ((0, 3, 1, 3, math.inf, math.inf),
         (3, 0, 4, math.inf, math.inf, math.inf),
         (1, 4, 0, math.inf, 7, 5),
         (3, math.inf, math.inf, 0, math.inf, 2),
         (math.inf, math.inf, 7, math.inf, 0, 4),
         (math.inf, math.inf, 5, 2, 4, 0))

vertex_count = len(graph)
weight = [math.inf]*vertex_count

start_vertex = 0
watched = {start_vertex}
weight[start_vertex] = 0
optimal_connections = [0]*vertex_count

while start_vertex != -1:          # цикл, пока не просмотрим все вершины
    for index, value in enumerate(graph[start_vertex]):
        if index not in watched:
            w = weight[start_vertex] + value
            if w < weight[index]:
                weight[index] = w
                # связываем вершину j с вершиной v
                optimal_connections[index] = start_vertex

    # выбираем следующий узел с наименьшим весом
    start_vertex = arg_min(weight, watched)
    if start_vertex >= 0:
        watched.add(start_vertex)

# формирование оптимального маршрута:
start = 0
end = 4
ret_end = end
optimal_path = [end]
while end != start:
    end = optimal_connections[optimal_path[-1]]
    optimal_path.append(end)

print(
    f'Оптимальный путь из вершины {start} в вершину {ret_end}:\n{optimal_path}')

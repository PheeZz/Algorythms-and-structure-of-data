import math


def get_max_vertex(vertex, graph, watched):
    _min = 0   # наименьшее допустимое значение
    vertex_index = -1
    for index, value in enumerate(graph[vertex]):
        if index in watched:
            continue

        if value[2] == 1:   # движение по стрелке
            if _min < value[0]:
                _min = value[0]
                vertex_index = index
        else:           # движение против стрелки
            if _min < value[1]:
                _min = value[1]
                vertex_index = index

    return vertex_index


def get_max_flow(point):
    w = [x[0] for x in point]
    return min(*w)


def update_weight(graph, points, flow):
    for point in points:
        if point[1] == -1:  # это исток
            continue

        direction = graph[point[2]][point[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        graph[point[1]][point[2]][0] -= flow * direction
        graph[point[1]][point[2]][1] += flow * direction

        graph[point[2]][point[1]][0] -= flow * direction
        graph[point[2]][point[1]][1] += flow * direction


graph = [[[0, 0, 1], [20, 0, 1], [30, 0, 1], [10, 0, 1], [0, 0, 1]],
         [[20, 0, -1], [0, 0, 1], [40, 0, 1], [0, 0, 1], [30, 0, 1]],
         [[30, 0, -1], [40, 0, -1], [0, 0, 1], [10, 0, 1], [20, 0, 1]],
         [[10, 0, -1], [0, 0, 1], [10, 0, -1], [0, 0, 1], [20, 0, 1]],
         [[0, 0, 1], [30, 0, -1], [20, 0, -1], [20, 0, -1], [0, 0, 1]],
         ]

vertex_count = len(graph)
start = 0    # вершина истока (нумерация с нуля)
end = 4     # вершина стока
# первая метка маршруто (a, from, vertex)
start_point = (math.inf, -1, start)
max_flow = []

j = start
while j != -1:
    current_vertex = start
    points = [start_point]
    watched = {start}

    while current_vertex != end:
        j = get_max_vertex(current_vertex, graph, watched)
        if j == -1:         # если следующих вершин нет
            if current_vertex == start:      # и мы на истоке
                break
            else:
                current_vertex = points.pop()[2]
                continue

        current_flow = graph[current_vertex][j][0] if graph[current_vertex][j][2] == 1 else graph[current_vertex][j][1]
        points.append((current_flow, j, current_vertex))
        watched.add(j)

        if j == end:    # если дошли до стока
            max_flow.append(get_max_flow(points))
            update_weight(graph, points, max_flow[-1])
            break

        current_vertex = j

max_flow = sum(max_flow)
print(f"Максимальный поток равен: {max_flow}")

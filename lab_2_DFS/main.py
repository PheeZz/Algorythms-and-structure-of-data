'''
3. Найти в заданном графе количество и состав компонент связности с
помощью поиска в глубину
'''

graph = {'A': set(['B', 'C']),
         'B': set(['D', 'E']),
         'C': set(['A']),
         'D': set(['E', 'F']),
         'E': set(['B', 'F']),
         'F': set(['A', 'E']),
         'G': set(['H']),
         'H': set(['G', 'I']),
         'I': set(['G', 'H'])
         }


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == end:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


dict_with_connected_points = {}
for points in graph:
    result = dfs(graph, points)
    dict_with_connected_points.update({points: result})

# unificate values in dictWithConnectedPoints
def unificate_values_in_dict(dictionary):
    for startKey in dictionary:
        for lenKey in dictionary:
            if dictionary[startKey] == dictionary[lenKey] and startKey is not lenKey:
                dictionary.update({startKey: None})

    # удаление пустых значений из словаря
    dictionary = {key: value for key,
                  value in dictionary.items() if value is not None}
    return dictionary


comps = unificate_values_in_dict(dict_with_connected_points)
index = 0
print(f'\nКоличество компонент связности в заданном графе: {len(comps)}')
for points in comps:
    index += 1
    print(
        f'Компонента связности №{index} состоит из вершин: {sorted(comps[points])}')
del index

'''
3. Найти в заданном графе количество и состав компонент связности с
помощью поиска в глубину
4. Найти в заданном орграфе количество и состав сильно связных
компонент с помощью поиска в глубину.
'''

from pprint import pprint
from queue import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'L': set(['M', 'N']),
         'M': set(['L', 'N']),
         'N': set(['L', 'M'])
         }


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


dictWithConnectedPoints = {}
for points in graph:
    result = dfs(graph, points)
    print(f'Список соединенных вершин с {points}: {result}')
    dictWithConnectedPoints.update({points: result})

# unificate values in dictWithConnectedPoints


def unificateValuesInDict(dictionary):
    for startKey in dictionary:
        for lenKey in dictionary:
            if dictionary[startKey] == dictionary[lenKey] and startKey is not lenKey:
                dictionary.update({startKey: None})

    # удаление пустых значений из словаря
    dictionary = {key: value for key,
                  value in dictionary.items() if value is not None}
    return dictionary


comps = unificateValuesInDict(dictWithConnectedPoints)
index = 0
print(f'Количество компонент связности в заданном графе: {len(comps)}')
for points in comps:
    index += 1
    print(f'Компонента связности №{index} состоит из вершин: {comps[points]}')

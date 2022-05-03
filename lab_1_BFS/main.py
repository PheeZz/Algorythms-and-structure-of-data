'''
1. Найти в заданном графе кратчайшие пути из заданной вершины до всех
остальных вершин с помощью поиска в ширину
2. Найти в заданном графе количество и состав компонент связности с
помощью поиска в ширину.
'''
from queue import deque
from pprint import pprint

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'],
         'L': ['M', 'N'],
         'M': ['L', 'N'],
         'N': ['L', 'M']}


def bfs(graph, startPoint, endPoint):
    queue = deque([(startPoint, list(startPoint))])
    while queue:
        (vertex, way) = queue.pop()
        try:
            for next in (set(graph[vertex]) - set(way)):
                if next == endPoint:
                    yield way + [next]
                else:
                    queue.appendleft((next, way+[next]))
        except KeyError:
            continue


def shortestWayBetween(graph, startPoint, endPoint):
    try:
        return next(bfs(graph, startPoint, endPoint))
    except StopIteration:
        return None


for points in graph:
    start = 'A'
    shortestWay = shortestWayBetween(graph, start, points)
    print(
        f'Кратчайший путь из вершины {start} в вершину {points}:  {shortestWay}')  # 1

print()


def isWayNone(graph, start, end):
    shortestWay = shortestWayBetween(graph, start, end)
    if shortestWay is None and start is not end:
        return True
    else:
        return False


def components(graph):
    tempDict = {}
    for key in graph:
        tempDict.setdefault(key)
        # создание словаря с отсутствующими путями для каждой верршины
    for start in graph:
        listOfAdds = list()
        for points in graph:
            if isWayNone(graph, start, points):
                listOfAdds.append(points)
                tempDict[start] = listOfAdds
            else:
                pass

    for startKey in tempDict:
        for lenKey in tempDict:
            if tempDict[startKey] == tempDict[lenKey] and startKey is not lenKey:
                tempDict.update({startKey: None})

    # удаление пустых значений из словаря
    tempDict = {key: value for key,
                value in tempDict.items() if value is not None}
    return tempDict


uniqComps = components(graph)


def printComps(uniqComps):
    count = 0
    for key in uniqComps:
        count += 1
        print(f'Компонента связности {count}: {uniqComps[key]}')


print(f'Количество компонент связности: {len(uniqComps)}')
printComps(uniqComps)

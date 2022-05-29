item_count = 4
back_pack_size = 5
items = [[1, 2], [2, 3], [3, 4], [4, 4]]
best_score = {'kit': [], 'weight': 0, 'cost': 0}


def to_binary(a, size):  # для определения
    a = bin(a)[2:]
    a = '0' * (size - len(a)) + a
    return a


for i in range(1, 2 ** item_count):
    # инициализируем наборы (1 - берем, 0 - не берем)
    items_set = list(to_binary(i, item_count))
    cost = 0  # стоимость взятых предметов
    weight = 0  # вес взятых предметов
    overflow = False  # флаг переполнения рюкзака
    for index, state in enumerate(items_set):
        if state == '1':
            # Если есть в наборе то добавляем в стоимость
            cost += items[index][1]
            weight += items[index][0]   # и вес
            if weight > back_pack_size:  # если переполнен, то ставим флаг
                overflow = True
                break
    print(items_set, cost, overflow)
    if not overflow:
        if best_score['cost'] < cost:  # если найден лучший вариант меняем значения
            best_score.update({'kit': [items_set], 'cost': cost})
        elif best_score['cost'] == cost:  # если найден идентичный нужному, добавляем набор
            best_score['kit'].append(items_set)

print(
    f'\nЛучший вариант: {best_score["kit"]}\nСо стоимостью: {best_score["cost"]}\nИ весом: {best_score["weight"]}')

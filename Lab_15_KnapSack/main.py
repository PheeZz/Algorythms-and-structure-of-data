
class backpack:
    def __init__(self, item_count, back_pack_size, items):
        self.item_count = item_count
        self.back_pack_size = back_pack_size
        self.items = items
        self.best_score = {'kit': [], 'weight': 0, 'cost': 0}

    def to_binary(self, string, size):  # для определения
        string = bin(string)[2:]
        string = '0' * (size - len(string)) + string
        return string

    def solve(self):
        for i in range(1, 2 ** self.item_count):
            # инициализируем наборы (1 - берем, 0 - не берем)
            items_set = list(self.to_binary(i, self.item_count))
            cost = 0  # стоимость взятых предметов
            weight = 0  # вес взятых предметов
            overflow = False  # флаг переполнения рюкзака
            for index, state in enumerate(items_set):
                #print(index, state, items_set)
                if state == '1':
                    # Если есть в наборе то добавляем в стоимость
                    cost += items[index][1]
                    weight += items[index][0]   # и вес
                    if weight > self.back_pack_size:  # если переполнен, то ставим флаг
                        overflow = True
                        break
            print(items_set, cost, overflow)
            if not overflow:
                # если найден лучший вариант меняем значения
                if self.best_score['cost'] < cost:
                    self.best_score.update({'kit': [items_set], 'cost': cost})
                # если найден идентичный нужному, добавляем набор
                elif self.best_score['cost'] == cost:
                    self.best_score['kit'].append(items_set)


items = [[1, 2], [2, 3], [3, 4], [4, 4]]

test = backpack(4, 5, items)
test.solve()
print(
    f'\nЛучший вариант: {test.best_score["kit"]}\nСо стоимостью: {test.best_score["cost"]}\nИ весом: {test.best_score["weight"]}')

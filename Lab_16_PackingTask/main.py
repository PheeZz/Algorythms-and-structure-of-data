import math
from time import sleep


# перевод в N-мерную систему счисления c дополнением до количества предметов
def inNsystem(index, boxes, item_count):
    res = []
    while index > 0:
        res.append(index % boxes)
        index = index // boxes
    res.reverse()
    for _ in range(item_count - len(res)):
        res.insert(0, 0)  # дополняем массив нулями до количества предметов
    return res


#items = [4, 2, 6, 2, 1, 4]
items = [3]*6
item_count = len(items)
box_size = 6
_sum = 0
for weight in items:
    _sum += weight
max_boxes = math.ceil(_sum / box_size)  # оценка количества ящиков сверху
best_choice = None
while best_choice is None:  # пока не найден лучший набор
    for index in range(max_boxes ** item_count):
        not_valid = False  # проверка на валидность набора
        box_stored = [0] * max_boxes  # вес который хранит каждый ящик
        places = inNsystem(index, max_boxes, item_count)  # набор
        #print(places)
        for item, place in enumerate(places):
            box_stored[place] += items[item]  # загружаем в ящик
            if box_stored[place] > box_size:  # если перебор
                not_valid = True
                break
        #print(places, not_valid)
        #sleep(0.01)
        if not not_valid:
            best_choice = places
            break
    max_boxes += 1  # если не найден набор для такого количества ящиков увеличиваем на единицу
print(best_choice)
print(_sum)
print(sum(best_choice))

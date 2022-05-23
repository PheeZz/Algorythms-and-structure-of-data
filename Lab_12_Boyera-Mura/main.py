from random import randint

if randint(0, 1) == 0:
    text = 'abc da bcab cdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'


def create_shift_table(pattern):
    symbols = set()  # уникальные символы в паттерне
    shift = {}     # словарь смещений

    for i in range(len(pattern)-2, -1, -1):  # итерации от предпоследнего символа до первого
        if pattern[i] not in symbols:
            # ключ = смещение от конца образа
            shift[pattern[i]] = len(pattern)-i-1
            symbols.add(pattern[i])

    if pattern[len(pattern)-1] not in symbols:     # отдельно формируем последний символ
        shift[pattern[len(pattern)-1]] = len(pattern)

    shift['*'] = len(pattern)              # смещения для прочих символов
    print(shift)
    return shift

# Этап 2: поиск образа в строке


def boyer_mur(text, pattern):
    shift = create_shift_table(pattern)
    if len(text) >= len(pattern):
        # счетчик проверяемого символа в строке
        current_symbol_in_text = len(pattern)-1

        while(current_symbol_in_text < len(text)):
            k = 0  # все предыдущие символы перед current_symbol_in_text
            current_symbol_in_pattern = 0
            flBreak = False
            for current_symbol_in_pattern in range(len(pattern)-1, -1, -1):
                if text[current_symbol_in_text-k] != pattern[current_symbol_in_pattern]:
                    if current_symbol_in_pattern == len(pattern)-1:
                        # смещение, если не равен последний символ образа
                        text_shift = shift[text[current_symbol_in_text]] if shift.get(
                            text[current_symbol_in_text], False) else shift['*']
                    else:
                        # смещение, если не равен не последний символ образа
                        text_shift = shift[pattern[current_symbol_in_pattern]]

                    current_symbol_in_text += text_shift    # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1          # смещение для сравниваемого символа в строке

            if not flBreak:          # если дошли до начала образа, значит, все его символы совпали
                return f"образ найден по индексу {current_symbol_in_text-k+1}\n{pattern}\n{text}"
        else:
            return "образ не найден"
    else:
        return "Ошибка: длина образа больше длины строки"


print(boyer_mur(text, pattern))

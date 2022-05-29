from random import randint

if randint(0, 1) == 0:
    text = 'abcdabcabcdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'


def automaton_search(pattern, text):
    alphabet = get_unique_chars(pattern)
    automaton = get_automaton_for_substring(pattern)
    state = 0
    for index, char in enumerate(text):
        try:
            # переходим в следующее состояние из автомата
            state = automaton[state][alphabet.index(char)]
        except ValueError:  # если в алфавите образца нет буквы которая есть в алфавите текста
            state = 0
        if state == len(pattern):  # если дошли до последнего состояния
            return index - state + 1
    return -1


def get_automaton_for_substring(pattern):
    unique_chars = get_unique_chars(pattern)
    automaton = [[0 for _ in range(len(unique_chars))]
                 for _ in range(len(pattern))]
    automaton[0][0] = 1
    length = 0
    for i in range(1, len(pattern)):
        automaton[i] = automaton[length].copy()
        # алгоритм построения конечного автомата
        automaton[i][unique_chars.index(pattern[i])] = i + 1
        length = automaton[length][unique_chars.index(pattern[i])]
    return automaton


def get_unique_chars(pattern):
    unique = list()
    for i in pattern:
        if i not in unique:
            unique.append(i)
        # оптимизация проверки на повторение символов, чтобы исключить лишние циклы
        if len(unique) == len(set(pattern)):
            break
    return unique


# print(get_unique_chars(pattern))
print(f'\nИндекс первого совпадения:\n{automaton_search(pattern,text)}\n{text}\n{pattern}' if automaton_search(
    pattern, text) != -1 else 'Совпадений не найдено')

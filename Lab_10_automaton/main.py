from random import randint

if randint(0, 1) == 0:
    text = 'abcdabcabcdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'


class seeker:
    def __init__(self, text, pattert):
        self.text = text
        self.pattern = pattert

    def get_automaton_for_substring(self, pattern):
        unique_chars = self.get_unique_chars(pattern)
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

    def get_unique_chars(self, pattern):
        unique = list()
        for i in pattern:
            if i not in unique:
                unique.append(i)
            # оптимизация проверки на повторение символов, чтобы исключить лишние циклы
            if len(unique) == len(set(pattern)):
                break
        return unique

    def automaton_search(self):
        unique = self.get_unique_chars(self.pattern)
        automaton = self.get_automaton_for_substring(self.pattern)
        state = 0
        for index, char in enumerate(self.text):
            try:
                # переходим в следующее состояние из автомата
                state = automaton[state][unique.index(char)]
            except ValueError:  # если в алфавите образца нет буквы которая есть в алфавите текста
                state = 0
            if state == len(pattern):  # если дошли до последнего состояния
                return index - state + 1
        return -1


test = seeker(text, pattern)
result = test.automaton_search()
# print(get_unique_chars(pattern))
print(
    f'\nИндекс первого совпадения:\n{result}\n{test.text}\n{test.pattern}' if result != -1 else 'Совпадений не найдено')

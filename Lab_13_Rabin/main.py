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

    def get_hash_of_string(self, string, size):
        _hash = 0
        for index in range(len(string)):
            _hash += ord(string[index]) * \
                (size ** (len(string)-index))
        return _hash

    def RabinKarpSearch(self):
        size = len(set((self.text)))
        _hash = self.get_hash_of_string(self.pattern, size)
        for index in range(len(self.text) - len(pattern)):
            if _hash == self.get_hash_of_string(self.text[index:index + len(pattern)], size):
                return index
        return -1


test = seeker(text, pattern)
result = test.RabinKarpSearch()
print(
    f'\nИндекс первого совпадения:\n{result}\n{test.text}\n{test.pattern}' if result != -1 else 'Совпадений не найдено')

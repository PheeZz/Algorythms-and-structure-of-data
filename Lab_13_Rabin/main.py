from random import randint

if randint(0, 1) == 0:
    text = 'abcdabcabcdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'


def RabinKarpSearch(pattern, text):
    size = len(set((text)))
    _hash = get_hash_of_string(pattern, size)
    for index in range(len(text) - len(pattern)):
        if _hash == get_hash_of_string(text[index:index + len(pattern)], size):
            return index
    return -1


def get_hash_of_string(pattern, size):
    _hash = 0
    for index in range(len(pattern)):
        _hash += ord(pattern[index]) * (size ** (len(pattern)-index))
    return _hash


print(f'\nИндекс первого совпадения:\n{RabinKarpSearch(pattern,text)}\n{text}\n{pattern}' if RabinKarpSearch(
    pattern, text) != -1 else 'Совпадений не найдено')

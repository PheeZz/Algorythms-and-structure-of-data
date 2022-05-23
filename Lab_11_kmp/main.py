from random import randint

if randint(0, 1) == 0:
    text = 'abcdabcabcdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'


def suffix(pattern):
    suffix_is_prefix_max_len = [0]*len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            suffix_is_prefix_max_len[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                suffix_is_prefix_max_len[i] = 0
                i += 1
            else:
                j = suffix_is_prefix_max_len[j-1]
    return suffix_is_prefix_max_len


def kmp(text, pattern):
    suff_max_len = suffix(pattern)
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                print(f'Нашли совпадение, индекс: {i-j}\n{pattern}\n{text}')
                break
        else:
            if j > 0:
                j = suff_max_len[j-1]
            else:
                i += 1

    if i == len(text) and j != len(pattern):
        print(f"образ не найден\n{pattern}\n{text}")


kmp(text, pattern)

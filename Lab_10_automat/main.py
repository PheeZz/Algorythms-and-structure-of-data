from random import randint

if randint(0, 1) == 0:
    text = 'abcdabcabcdabcdab'
    pattern = "cda"
else:
    text = 'лилилось лилилась лилились'
    pattern = 'лилила'

def search_auto(string, pattern):
    index = -1
    for i in range(len(string)-len(pattern)+1):
        success = True
        for j in range(len(pattern)):
            if pattern[j] != string[i+j]:
                success = False
                break
        if success:
            index = i
            break
    return index




print(f'Индекс первого совпадения:\n{search_auto(text, pattern)}' if search_auto(text, pattern) != -1 else 'Совпадений не найдено')
print(text)

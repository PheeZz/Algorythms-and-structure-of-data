_input = [-20, -4, 6, 1, 18, 5, -3, 3, -2]
set_with_zero_summ = [_input[0]]
_sum = _input[0]
size = len(_input)
for i in range(1, size):
    if (abs(_sum + _input[i]) < abs(_sum)):
        _sum += _input[i]
        set_with_zero_summ.append(_input[i])
        print(set_with_zero_summ)
        print(sum(set_with_zero_summ))
if _sum == 0:
    for i, num in enumerate(set_with_zero_summ):
        print(num, end=' ')
else:
    print('no sets with greedy')

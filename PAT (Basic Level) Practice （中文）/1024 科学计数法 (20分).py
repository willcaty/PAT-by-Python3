# -*- coding=utf-8 -*-

n, m = input().split('E')
one = '' if n[0] == '+' else '-'
number = n[1:].replace('.', '')
zhi_shu = int(m[1:])
n_len = len(number)
result = ''
if zhi_shu == 0:
    print(one + number[1:])
elif m[0] == '+':
    w = zhi_shu + 1 - n_len
    if w < 0:
        result = one + number[:zhi_shu + 1] + '.' + number[zhi_shu + 1:]
    else:
        result = one + number + '0' * w
else:
    result = one + '0.' + '0' * (zhi_shu - 1) + number
print(result)

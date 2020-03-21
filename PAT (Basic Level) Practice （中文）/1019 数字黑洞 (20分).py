# -*- coding=utf-8 -*-
n = f'{int(input()):04d}'
while True:
    a = ''.join(sorted(n, reverse=True))
    b = ''.join(sorted(n))
    n = f'{int(a) - int(b):04d}'
    print(f'{a} - {b} = {n}')
    if n in ('0000', '6174'):
        break

# -*- coding: utf-8 -*-

n = list(map(int, input().split()))

result = []
for i in range(0, len(n), 2):
    coefficient = n[i]  # 系数
    exponent = n[i + 1]  # 指数
    if exponent:
        result.append(str(coefficient * exponent))
        result.append(str(exponent - 1))

print(' '.join(result)) if len(result) else print('0 0')

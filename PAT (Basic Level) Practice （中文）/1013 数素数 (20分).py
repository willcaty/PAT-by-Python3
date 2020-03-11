# -*- coding: utf-8 -*-

n = list(map(int, input().split()))
max_n = 110000
result = ['2']
flag = [True] * (max_n + 2)
p = 3
while len(result) <= n[1]:
    result.append(p)
    for i in range(2 * p, max_n + 1, p):
        flag[i] = False
    while 1:
        p += 2
        if flag[p] is True:
            break
result = list(map(str, result[n[0] - 1:n[1]]))
while len(result) > 0:
    if len(result) <= 10:
        print(' '.join(result[0:10]), end='')
    else:
        print(' '.join(result[0:10]))
    for i in result[0:10]:
        result.remove(i)

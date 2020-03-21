# -*- coding=utf-8 -*-

A, B, D = list(map(int, input().split()))
number = A + B
a = [i for i in range(D)]
b = []
while True:
    s = number // D  # 商
    y = number % D  # 余数
    b.append(y)
    if s == 0:
        break
    number = s
b.reverse()
for i in b:
    print(a[i], end='')

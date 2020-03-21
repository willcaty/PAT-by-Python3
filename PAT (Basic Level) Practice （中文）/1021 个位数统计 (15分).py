# -*- coding=utf-8 -*-
n = list(input())

temp = {}
for i in n:
    temp[i] = n.count(i)

for i in sorted(temp):
    print(f'{i}:{temp[i]}')

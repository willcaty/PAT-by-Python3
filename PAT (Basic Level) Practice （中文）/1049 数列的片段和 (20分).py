# -*- coding=utf-8 -*-

n = int(input())
l = list(map(float, input().split()))
result = 0.00
len_l = len(l)
for i in range(len_l):
    result += l[i] * len_l * (i + 1)
    len_l -= 1

print(f'{result:.2f}')

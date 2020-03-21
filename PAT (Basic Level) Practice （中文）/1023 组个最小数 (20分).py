# -*- coding: utf-8 -*-
n = input().split()
temp = []
zero = ''
for i in range(len(n)):
    for j in range(int(n[i])):
        temp.append(str(i))
        if str(i) == '0':
            zero += '0'
        else:
            print(str(i) + zero, end='')
            zero = ''

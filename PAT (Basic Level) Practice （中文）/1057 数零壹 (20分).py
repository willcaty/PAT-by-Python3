# -*- coding: utf-8 -*-

str_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
            'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26}  # 字母数值对照

n = input()
result = 0
for i in n:  # 循环字符串
    result += str_dict.get(i.lower(), 0)  # 取小写的字符串当成key去取值，如果没有给默认值0
# 获取个数
zero = bin(result)[2:].count('0')
one = bin(result)[2:].count('1')
# 输出
print(result and f'{zero} {one}' or '0 0')

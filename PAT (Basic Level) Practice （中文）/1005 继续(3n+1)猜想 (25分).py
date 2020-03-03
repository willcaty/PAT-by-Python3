# -*- coding: utf-8 -*-

n = int(input())
input_list = list(map(int, input().split()))
key = []  # 计算过的值


def callatz(list_):
    for n in list_:  # 循环输入进来的列表
        if n not in key:  # 当前值没有计算过
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = (3 * n + 1) / 2
                key.append(int(n))


callatz(input_list)
key_list = []
for i in input_list:
    if i not in key:
        key_list.append(i)
key_list.sort(reverse=True)
output = ''
for i in key_list:
    output = output + str(i) + ' '
print(output[0:-1])

# -*- coding: utf-8 -*-

n = int(input())
input_list = [input().strip().split() for i_ in range(n)]
input_list.sort(key=lambda x: int(x[2]), reverse=True)
print(input_list[0][0], input_list[0][1])
print(input_list[-1][0], input_list[-1][1])

# -*- coding: utf-8 -*-
num = int(input())
B = num // 100  # 取整除
S = (num % 100) // 10  # 取模后，取整除
N = num % 10

print("B" * B+"S" * S, end="")
for i in range(N):
    print(i + 1, end="")
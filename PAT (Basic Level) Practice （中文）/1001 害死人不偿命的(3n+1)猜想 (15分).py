# -*- coding=utf-8 -*-

n = int(input())  # 接收参数
step_number = 0
while n != 1:  # 直到n=1返回步数
    if n % 2 == 0:  # 判断奇偶
        n /= 2
    else:
        n = (3 * n + 1) / 2
    step_number += 1  # 步数+1
print(step_number)

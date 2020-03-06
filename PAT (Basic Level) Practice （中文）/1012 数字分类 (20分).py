# -*- coding: utf-8 -*-

input_list = list(map(int, input().split()))
A1 = A2 = A3 = A4 = A5 = len_4 = flag = 0
for i in input_list[1:]:
    r = i % 5
    #  能被 5 整除的数字中所有偶数的和
    if i % 10 == 0:
        A1 += i
    # 将被 5 除后余 1 的数字按给出顺序进行交错求和
    elif r == 1:
        A2 += (-1) ** flag * i
        flag += 1
    # 被 5 除后余 2 的数字的个数
    elif r == 2:
        A3 += 1
    # 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
    elif r == 3:
        A4 += i
        len_4 += 1
    # 被 5 除后余 4 的数字中最大数字。
    elif r == 4:
        A5 = max(A5, i)

A1 = A1 and A1 or 'N'
A3 = A3 and A3 or 'N'
A5 = A5 and A5 or 'N'
A4 = A4 and f'{A4 / len_4:.1f}' or 'N'
A2 = A2 if flag else 'N'
print(A1, A2, A3, A4, A5)

# -*- coding=utf-8 -*-

N, D = list(map(int, input().split()))

total_amount = 0  # 最大收益
stock = list(map(float, input().split()))
amount = list(map(float, input().split()))

temp = [[amount[i] / stock[i], amount[i], stock[i]] for i in range(N)]

temp.sort(key=lambda x: (x[0], x[1]), reverse=True)

for i in temp:
    if D >= i[2]:
        D -= i[2]
        total_amount += i[1]
    else:
        total_amount += D * i[0]
        break
print(f'{total_amount:.2f}')

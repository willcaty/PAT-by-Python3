# -*- coding: utf-8 -*-

for i in range(int(input())):
    m = list(map(int, input().split()))
    print(m[0] + m[1] > m[2] and f'Case #{i + 1}: true' or f'Case #{i + 1}: false')

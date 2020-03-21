# -*- coding: utf-8 -*-

A, DA, B, DB = input().split()
result_a = A.count(DA) * DA
result_b = B.count(DB) * DB

print(int(result_a and result_a or 0) + int(result_b and result_b or 0))

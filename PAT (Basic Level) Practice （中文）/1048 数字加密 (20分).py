# -*- coding=utf-8 -*-
A, B = input().split()
max_len = max(len(A), len(B))
A, B = f'{int(A):0{max_len}d}'[::-1], f'{int(B):0{max_len}d}'[::-1]
d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
     7: '7', 8: '8', 9: '9', 10: 'J', 11: 'Q', 12: 'K'}
result = ''
for i in range(max_len):
    odd = d.get((int(A[i]) + int(B[i])) % 13)
    even = str((int(B[i]) - int(A[i]) + 10) % 10)
    result += (i + 1) % 2 and odd or even

print(result[::-1])

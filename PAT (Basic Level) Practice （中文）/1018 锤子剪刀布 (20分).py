# -*- coding=utf-8 -*-
import sys

n = int(input())

# C 锤子，J剪刀，B布
win_B_a = win_C_a = win_J_a = 0
win_B_b = win_C_b = win_J_b = 0
draw = 0
for i_ in range(n):
    i = sys.stdin.readline().split()
    if i[0] == 'C' and i[1] == 'J':
        win_C_a += 1
    elif i[0] == 'C' and i[1] == 'B':
        win_B_b += 1
    elif i[0] == 'B' and i[1] == 'J':
        win_J_b += 1
    elif i[0] == 'B' and i[1] == 'C':
        win_B_a += 1
    elif i[0] == 'J' and i[1] == 'C':
        win_C_b += 1
    elif i[0] == 'J' and i[1] == 'B':
        win_J_a += 1
    else:
        draw += 1
a_win = win_B_a + win_C_a + win_J_a
a_fail = n - a_win - draw
b_win = win_B_b + win_C_b + win_J_b
b_fail = n - draw - b_win
print(a_win, draw, a_fail)
print(b_win, draw, b_fail)
temp_a = ''
if win_B_a >= win_J_a and win_B_a >= win_C_a:
    temp_a = 'B'
elif win_C_a > win_B_a and win_C_a >= win_J_a:
    temp_a = 'C'
else:
    temp_a = 'J'

temp_b = ''
if win_B_b >= win_J_b and win_B_b >= win_C_b:
    temp_b = 'B'
elif win_C_b > win_B_b and win_C_b >= win_J_b:
    temp_b = 'C'
else:
    temp_b = 'J'
print(temp_a, temp_b)

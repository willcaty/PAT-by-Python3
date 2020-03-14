# -*- coding=utf-8 -*-
import math

R1, P1, R2, P2 = list(map(float, input().split()))

A = R1 * math.cos(P1) * R2 * math.cos(P2) - R1 * math.sin(P1) * R2 * math.sin(P2)
B = R1 * math.cos(P1) * R2 * math.sin(P2) + R2 * math.cos(P2) * R1 * math.sin(P1)

print(-0.005 <= A < 0 and '0.00' or '%.2f' % A, end='')
if B >= 0:
    print(f'+{B:.2f}i')
elif -0.005 <= B < 0:
    print('+0.00i')
elif B < 0:
    print(f'{B:.2f}i')

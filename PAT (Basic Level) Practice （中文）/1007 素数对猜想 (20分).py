# -*- coding: utf-8 -*-

n = int(input())
step = 2
contrast = [True] * (n + 2)
result = []

while step <= n:
    result.append(step)
    for i in range(step * 2, n + 1, step):
        contrast[i] = False
    while step <= n:
        step += 1
        if contrast[step]:
            break

print(len([i for i in range(len(result) - 1) if result[i + 1] - result[i] == 2]))


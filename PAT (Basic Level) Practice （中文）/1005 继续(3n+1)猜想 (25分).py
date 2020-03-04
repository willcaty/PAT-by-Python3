# -*- coding: utf-8 -*-

n = int(input())
s = set()  # 所有遍历过的数字的集合
sr = set()  # 关键数的列表
for i in map(int, input().split()):
    if i not in s:
        sr.add(i)
    while i not in s:
        s.add(int(i))
        i = i % 2 and (3 * i + 1) / 2 or i / 2
    sr.discard(i)
print(' '.join(map(str, sorted(sr, reverse=True))))
